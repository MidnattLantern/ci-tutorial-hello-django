from django.db import models


class Item(models.Model):
    """
    Name and mdoel
    """
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # something else than "Item object (indx)"
    def __str__(self):
        return self.name
