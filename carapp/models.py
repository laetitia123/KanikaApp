from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class CarCategory(models.Model):
    categoryName=(
        ('Toyota','Toyota'),
        ('Cross country','Cross country'),
        ('Vox wagen','Vox wagen'),
        ('Suzuki','Suzuki'),
        ('Mahindra','Mahindra'),
        ('Honda','Honda'),
        ('Hyunda','Hyunda'),
        ('Volvo','Volvo'),
        ('Daihatsu','Daihatsu'),
        
    )
    categoryPart=models.CharField(max_length=40,choices=categoryName)
    categoryImage=models.ImageField(upload_to='category/')

    def __str__(self):
        return self.categoryPart


    #  @classmethod
    # def filter_by_location(cls, id):
    #    image= Image.objects.filter(location_id=id)
    #    return image
class Partners(models.Model):
    partner_name = models.CharField(max_length=60,null=True)
    description= models.CharField(max_length=300,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE, blank=True,null=True)
    email = models.CharField(max_length=60,null=True)
    partner_image = models.ImageField(upload_to='partner/',null=True)
    approved = models.BooleanField(default=False )
    phone= models.CharField(max_length=60,null=True)
    def __str__(self):
        return str(self.partner_name)
    def save_partner(self):
        self.save()

class SpareParts(models.Model):
    nameChoose = (
                  ('Head lights', 'Head lights'),
                  ('Brake lights', 'Brake lights'),
                  ('Tail lights', 'Tail lights'),
                  ('Tail gate', 'Tail gate'),
                  ('Mirrors', 'Mirrors'),
                  ('Hoods', 'Hoods'),
                  ('Window', 'Window'),
                  ('Door', 'Door'),
                  ('Tyres', 'Tyres'),
                  ('Petrol tank', 'Petrol tank'),
                  ('Roof', 'Roof'),
                  ('Steering wheel', 'Steering wheel'),
                  ('Engine', 'Engine'),
                  ('wheel tyres','wheel tyres'),

                  )
    namePart= models.CharField(max_length=40, choices=nameChoose)
    price = models.IntegerField()
    locationChoose = (
        ('Gatsata', 'Gatsata'),
        ('Nyamirambo', 'Nyamirambo'),
        ('Remera', 'Remera'),
        ('Nyabugogo', 'Nyabugogo'),
        )
    locationPart = models.CharField(max_length=40, choices=locationChoose)
    ImagePart= models.ImageField(upload_to='spareparts/')
    Phone = models.IntegerField()
    user=models.ForeignKey(User,on_delete= models.CASCADE,null=True)
    categoryName = (
        ('Toyota', 'Toyota'),
        ('Cross country', 'Cross country'),
        ('Vox wagen', 'Vox wagen'),
        ('Suzuki', 'Suzuki'),
        ('Mahindra', 'Mahindra'),
        ('Honda', 'Honda'),
        ('Hyunda', 'Hyunda'),
        ('Volvo', 'Volvo'),
        ('Daihatsu', 'Daihatsu'),

    )

    categoryPart = models.CharField(max_length=40, choices=categoryName)
    categoryImage = models.ImageField(upload_to='category/',blank=True)
    carCat = models.ManyToManyField(CarCategory)
    partner_name = models.ForeignKey(Partners,on_delete= models.CASCADE,blank=True,null=True)
    

    def __str__(self):
        return self.namePart

    @classmethod
    def search_by_categoryname(cls,search_term):
        name = cls.objects.filter(categoryPart__icontains = search_term)
        return name

class Cart(models.Model):
    sparePart = models.ManyToManyField(SpareParts, null=True, blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    actives = models.BooleanField(default=True)

    def __unicode__(self):
        return "cart id: %s" % (self.id)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        default='default.jpg', upload_to='profiles/')
    country = models.TextField(max_length=100)
    contact = models.IntegerField(default=None, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.country

    def save_profile(self):
        self.save()

    # .............    building API.............................

class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class CarMerch(AbstractBaseUser, models.Model):
        email = models.EmailField(verbose_name="email", max_length=60, unique=True)
        username = models.CharField(max_length=30, unique=True)
        date_joined = models.DateTimeField(
            verbose_name='date joined', auto_now_add=True)
        last_login = models.DateTimeField(
            verbose_name='last login', auto_now=True)
        is_admin = models.BooleanField(default=False)
        is_active = models.BooleanField(default=True)
        is_staff = models.BooleanField(default=False)
        is_superuser = models.BooleanField(default=False)

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['username']

        objects = MyAccountManager()

        def __str__(self):
            return self.email

        # For checking permissions. to keep it simple all admin have ALL permissons
        def has_perm(self, perm, obj=None):
            return self.is_admin

        # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
        def has_module_perms(self, app_label):
            return True

        def get_short_name(self):
            return self.username

            
        


# class partner(models.Model):

#     image =models.ImageField(upload_to='uploads/',blank=True,null=True)
#     sparePart=models.ManyToManyField(SpareParts,null=True,blank=True)
#     CarCategory=models.ManyToManyField(CarCategory,null=True,blank=True)
#     user=models.ForeignKey(User,on_delete= models.CASCADE,null=True)
#     # approved = models.BooleanField(default=False )

#     @classmethod
#     def get_images(cls):
#         image=partner.objects.all()
#         return image

#     @classmethod
#     def get_image_by_id(cls,id):
#         image=partner.objects.filter(id=partner.id)
#         return image

#     @classmethod
#     def filter_By_category(cls, id):
#         locate = CarCategory.objects.filter(location_id=id)
#         return locate


# class User(models.Model):
#     pic=ImageField(upload_to="profiless")
    


