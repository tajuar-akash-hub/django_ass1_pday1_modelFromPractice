from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField( max_length=50)
    roll = models.IntegerField()
    auto_field= models.AutoField(primary_key=True)
    address= models.TextField()
    big_integer_field= models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    date_field = models.DateField()
    duration_field = models.DurationField()
    email_field=models.EmailField()
    file_field = models.FileField( upload_to="./first_app/uploads", max_length=100)
    ip_address = models.GenericIPAddressField( protocol="both", unpack_ipv4=False)
    time_field = models.TimeField()
    
    
    
    def __str__(self) -> str:
        return f'name = {self.name}, roll= {self.roll} , address = {self.address}'
    

