from djongo import models


class MyForm(models.Model):
    name = models.CharField(verbose_name="name", max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "MyForms"
        verbose_name = "MyForm"


class Fields(models.Model):
    form = models.ForeignKey(MyForm, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name="email address", max_length=255)
    phone = models.CharField(verbose_name="phone", max_length=255)
    text = models.TextField(verbose_name="text")
    date = models.DateField(verbose_name="date")

    class Meta:
        verbose_name_plural = "Fields"
        verbose_name = "Field"
