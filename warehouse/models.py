from django.db import models

class Box(models.Model):
    name = models.CharField(max_length=50)
    dim1 = models.IntegerField(help_text="Smallest dimension")
    dim2 = models.IntegerField(help_text="Middle dimension")
    dim3 = models.IntegerField(help_text="Largest dimension")
    max_weight = models.IntegerField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        ordering = ['cost']  # Checks cheapest box first!

    def save(self, *args, **kwargs):
        dims = sorted([self.dim1, self.dim2, self.dim3])
        self.dim1, self.dim2, self.dim3 = dims
        super().save(*args, **kwargs)