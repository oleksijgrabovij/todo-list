from django.test import TestCase
from django.urls import reverse
from todo.models import Tag, Task
from todo.forms import TagForm, TaskForm


class ModelTests(TestCase):
    def test_tag_str_representation(self):
        tag = Tag.objects.create(name="Work")
        self.assertEqual(str(tag), "Work")

    def test_task_str_representation(self):
        task = Task.objects.create(content="Do laundry")
        self.assertEqual(str(task), "Do laundry")


class FormTests(TestCase):
    def test_tag_form_valid_data(self):
        form = TagForm(data={"name": "Urgent"})
        self.assertTrue(form.is_valid())

    def test_task_form_valid_data(self):
        # Create a tag first to satisfy the ManyToMany requirement
        tag = Tag.objects.create(name="Work")

        # Pass both content and the tag ID
        form = TaskForm(data={
            "content": "Buy milk",
            "tags": [tag.id]
        })

        # We add form.errors so if it fails, it prints exactly which field is missing
        self.assertTrue(form.is_valid(), form.errors)


class ViewTests(TestCase):
    def setUp(self):
        # Create test data before each test
        self.tag = Tag.objects.create(name="Home")
        self.task = Task.objects.create(content="Clean room", is_done=False)

    def test_task_list_view(self):
        response = self.client.get(reverse("todo:task-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/task_list.html")
        self.assertContains(response, "Clean room")

    def test_task_status_update_via_post(self):
        # Check if the status changes via POST request
        url = reverse("todo:task-toggle", kwargs={"pk": self.task.id})
        response = self.client.post(url)

        # Refresh the object from the database
        self.task.refresh_from_db()

        # Check that the status has changed to True
        self.assertTrue(self.task.is_done)
        # Check if a redirect to the home page occurred
        self.assertRedirects(response, reverse("todo:task-list"))
