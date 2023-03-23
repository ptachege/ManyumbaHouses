from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_save
from django.utils.text import slugify
import random
import string


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_account_type = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)    
    visitorcount = models.IntegerField(default=0)
    account_verified = models.BooleanField(default=False)
    profile_image = CloudinaryField('image', blank=True, null=True)


    def __str__(self):
        return self.user.username



# ===============various status include :: For rent, For sale, For lease ====================
class PropertyStatus(models.Model):
    property_status = models.CharField(max_length=600)
    description = models.CharField(max_length=600, blank=True, null=True)

    class Meta:
        """Meta definition for PropertyStatus."""

        verbose_name = 'PropertyStatus'
        verbose_name_plural = 'PropertyStatus'

    def __str__(self):
        return self.property_status


class LandSizes(models.Model):
    size = models.CharField(max_length=600)

    class Meta:
        verbose_name = 'LandSizes'
        verbose_name_plural = 'LandSizes'

    def __str__(self):
        return self.size


# ==============features include : : Air conditioners , dryer , etc
class Features(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Features'
        verbose_name_plural = 'Features'


    def __str__(self):
        return self.name



# ===========type of house ie commercial, residential etc
class Type(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# ==========agents======

class Agents(models.Model):
    agent_name = models.CharField(max_length=200)
    picture = CloudinaryField('image')
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Agents'
        verbose_name_plural = 'Agents'



    def __str__(self):
        return self.agent_name


class Cities(models.Model):
    city_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Cities'
        verbose_name_plural = 'Cities'


    def __str__(self):
        return self.city_name


class Properties(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)    
    property_title = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True, unique=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    status = models.ForeignKey(PropertyStatus, on_delete=models.CASCADE)

    units = models.IntegerField(default=0, blank=True, null=True)
    available_rooms = models.IntegerField(default=0, blank=True, null=True)
    default_house_type = models.CharField(
        max_length=100, blank=True, null=True)

    available = models.BooleanField(default=True)
    price = models.IntegerField(default=0)
    security_deposit = models.IntegerField(default=0, blank=True, null=True)
    
    area_size = models.CharField(max_length=200, blank=True, null=True)
    landsize = models.ForeignKey(LandSizes, on_delete=models.CASCADE, blank=True, null=True)

    bedrooms = models.IntegerField(default=0)
    rooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    garages = models.IntegerField(default=0)
    year_built = models.CharField(max_length=100, blank=True, null=True)

    # map
    street_name = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.CharField(max_length=200, blank=True, null=True)

    # physica description
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    street = models.CharField(max_length=200, blank=True, null=True)
    
    # media
    video_url = models.CharField(max_length=1000, blank=True, null=True)
    virtual_tour_link = models.CharField(max_length=1000, blank=True, null=True)

    # contact 
    publish = models.BooleanField(default=True)

    managed_by_manyumba = models.BooleanField(default=False)

    featured_image = CloudinaryField('image')

    approved_by_admin = models.IntegerField(default=0, blank=True, null=True)


    # amenities
    Water = models.BooleanField(default=False)
    Electricity = models.BooleanField(default=False)
    WFI = models.BooleanField(default=False)
    Ac = models.BooleanField(default=False)
    Gateman = models.BooleanField(default=False)
    Parking = models.BooleanField(default=False)
    Swimming_Pool = models.BooleanField(default=False)
    Balcony = models.BooleanField(default=False)
    Gym = models.BooleanField(default=False)
    Play_Area = models.BooleanField(default=False)
    Internet = models.BooleanField(default=False)

    ElectricSupply = models.BooleanField(default=False)
    WaterSupply = models.BooleanField(default=False)
    RainWaterDrainage = models.BooleanField(default=False)
    DomesticSewage = models.BooleanField(default=False)


    BusinessLounge = models.BooleanField(default=False)
    Majortransportlinks = models.BooleanField(default=False)
    MeetingRooms = models.BooleanField(default=False)
    CCTV = models.BooleanField(default=False)
    Elevator = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Properties'
        verbose_name_plural = 'Properties'


    def __str__(self):
        return self.property_title

    def return_all_units(self):
        return self.units

    def return_vacant_units(self):
        return self.available_rooms

    def calculate_occupancy(self):
        modulus =self.units -  self.available_rooms
        occupancy = (modulus / self.units) * 100
        return occupancy
    
    def return_other_images(self):
        this_property_id = self.id
        all_images = PropertyImages.objects.filter(property__id=this_property_id)
        return all_images


class Tenant(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    t_user = models.ForeignKey(User, related_name='t_user', on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=10, blank=True)
    email = models.EmailField()
    contact = models.CharField(max_length=100)
    id_card = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    # property media  


class House(models.Model):
    apartment = models.ForeignKey(Properties, on_delete=models.CASCADE)
    house_code = models.CharField(max_length=1000, blank=True, null=True)
    house_type = models.CharField(max_length=200)
    rent = models.IntegerField(default=0)
    deposit = models.IntegerField(default=0)
    arrears = models.IntegerField(default=0)
    vacant = models.BooleanField(default=True)
    house_featured_image = CloudinaryField('image')

    def __str__(self):
        return str(self.house_code)


class Lease(models.Model):
    apartment = models.ForeignKey(Properties, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    lease_start_date = models.DateField(auto_now_add=True)
    lease_end_date = models.DateField()
    lease_documents = models.FileField(blank=True, null=True)
    current_status = models.BooleanField(default=False)
    running_balance = models.FloatField(default=0, blank=True, null=True)

    def __str__(self):
        return str(self.id)

    def return_active_lease(self):
        return 3

class VacateNotice(models.Model):
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE)
    vacate_date = models.CharField(max_length=1000)
    remarks = models.CharField(max_length=1000, blank=True, null=True)
    vacated = models.BooleanField(default=False)
    

    def __str__(self):
        return str(self.lease)


class FloorPlans(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    plan_title = models.CharField(max_length=100)
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=1)
    plan_size = models.IntegerField(default=1)
    plan_image = CloudinaryField('image', blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    class Meta:
        verbose_name = 'FloorPlans'
        verbose_name_plural = 'FloorPlans'


    def __str__(self):
        return self.plan_title



class PropertyDocuments(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    document = models.FileField(blank=True, null=True)



class PropertyImages(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    home_tag = models.CharField(max_length=100)
    featured = models.BooleanField(default=False)

    class Meta:

        verbose_name = 'PropertyImages'
        verbose_name_plural = 'PropertyImages'

    def __str__(self):
        return self.home_tag
 
class AdditionalDetails(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'AdditionalDetails'
        verbose_name_plural = 'AdditionalDetails'


    def __str__(self):
        return self.title


class Invoice(models.Model):
    # apartment = models.ForeignKey(Properties, on_delete=models.CASCADE)
    # house = models.ForeignKey(House, on_delete=models.CASCADE)
    # tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE)
    amount_incurred = models.FloatField(default=0)
    fully_paid = models.BooleanField(default=False)
    date_generated = models.DateField()
    amount_paid = models.FloatField(default=0, blank=True, null=True)
    amount_due = models.FloatField(default=0, blank=True, null=True)
    previous_over_dues = models.FloatField(default=0, blank=True, null=True)
    date_paid = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.id)


# class PaidRent(models.Model):
#     apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
#     house = models.ForeignKey(House, on_delete=models.CASCADE)
#     lease = models.ForeignKey(
#         Lease, on_delete=models.CASCADE, blank=True, null=True)
#     tenant = models.ForeignKey(
#         Tenant, on_delete=models.CASCADE, blank=True, null=True)
#     amount_paid = models.FloatField()
#     payment_for = models.DateField(blank=True, null=True)
#     date_paid = models.DateField()

#     def __str__(self):
#         return str(self.id)


class MorgageLeads(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=100, null=True, blank='True')
    phone = models.CharField(max_length=100, null=True, blank='True')
    email = models.CharField(max_length=100, null=True, blank='True')
    employment_type = models.CharField(max_length=100, null=True, blank='True')
    gross_income = models.CharField(max_length=100, null=True, blank='True')
    convinient_time = models.CharField(max_length=100, null=True, blank='True')
    property_price = models.IntegerField(null=True, blank='True')

    class Meta:

        verbose_name = 'MorgageLeads'
        verbose_name_plural = 'MorgageLeadss'

    def __str__(self):
        return self.full_name


class RelocationLeads(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=100, null=True, blank='True')
    phone = models.CharField(max_length=100, null=True, blank='True')
    email = models.CharField(max_length=100, null=True, blank='True')
    current_town = models.CharField(max_length=100, null=True, blank='True')
    employment_type = models.CharField(max_length=100, null=True, blank='True')
    gross_income = models.CharField(max_length=100, null=True, blank='True')
    convinient_time = models.CharField(max_length=100, null=True, blank='True')
    property_rent = models.IntegerField(null=True, blank='True')
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    completed = models.BooleanField(default=False)

    class Meta:

        verbose_name = 'RelocationLeads'
        verbose_name_plural = 'RelocationLeads'

    def __str__(self):
        return self.full_name


class Tours(models.Model):

    property = models.ForeignKey(Properties, on_delete=models.CASCADE, blank=True, null=True)    
    full_name = models.CharField(max_length=100, null=True, blank='True')
    phone = models.CharField(max_length=100, null=True, blank='True')
    tour_date = models.CharField(max_length=100, null=True, blank='True')
    message = models.CharField(max_length=100, null=True, blank='True')
    visited = models.BooleanField(default=False)
    mark_as_span = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Tours'
        verbose_name_plural = 'Tours'

    def __str__(self):
        return self.full_name



def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.property_title)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug, randstr=random_string_generator(size=4))

        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


def pre_save_receiver(sender, instance, *args, **kwargs):
    print(instance.slug)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender=Properties)
