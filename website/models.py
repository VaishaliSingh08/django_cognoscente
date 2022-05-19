# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Blog(models.Model):
    b_id_pk = models.BigAutoField(primary_key=True)
    b_heading_1 = models.CharField(max_length=200)
    b_desc_1 = models.CharField(max_length=3000)
    b_desc_2 = models.CharField(max_length=3000)
    b_desc_3 = models.CharField(max_length=3000)
    b_desc_4 = models.CharField(max_length=3000)
    b_desc_5 = models.CharField(max_length=3000)
    b_desc_6 = models.CharField(max_length=3000)
    b_desc_7 = models.CharField(max_length=3000)
    b_desc_8 = models.CharField(max_length=3000)
    b_desc_9 = models.CharField(max_length=3000)
    b_desc_10 = models.CharField(max_length=3000)
    b_image_1 = models.CharField(max_length=200)
    b_name = models.CharField(max_length=200)
    b_heading_2 = models.CharField(max_length=200)
    b_heading_3 = models.CharField(max_length=200)
    b_heading_4 = models.CharField(max_length=200)
    b_heading_5 = models.CharField(max_length=200)
    b_heading_6 = models.CharField(max_length=200)
    b_heading_7 = models.CharField(max_length=200)
    b_heading_8 = models.CharField(max_length=200)
    b_heading_9 = models.CharField(max_length=200)
    b_heading_10 = models.CharField(max_length=200)
    b_desc_11 = models.CharField(max_length=3000)
    b_desc_12 = models.CharField(max_length=3000)
    b_desc_13 = models.CharField(max_length=3000)
    b_desc_14 = models.CharField(max_length=3000)
    b_desc_15 = models.CharField(max_length=3000)
    b_desc_16 = models.CharField(max_length=3000)
    b_desc_17 = models.CharField(max_length=3000)
    b_desc_18 = models.CharField(max_length=3000)
    b_desc_19 = models.CharField(max_length=3000)
    b_desc_20 = models.CharField(max_length=3000)
    b_image_2 = models.CharField(max_length=200)
    b_image_3 = models.CharField(max_length=200)
    b_image_4 = models.CharField(max_length=200)
    b_image_5 = models.CharField(max_length=200)
    b_image_6 = models.CharField(max_length=200)
    b_image_7 = models.CharField(max_length=200)
    b_image_8 = models.CharField(max_length=200)
    b_image_9 = models.CharField(max_length=200)
    b_image_10 = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'blog'


class CaptchaCaptchastore(models.Model):
    challenge = models.CharField(max_length=32)
    response = models.CharField(max_length=32)
    hashkey = models.CharField(unique=True, max_length=40)
    expiration = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'captcha_captchastore'


class Contact(models.Model):
    c_id_pk = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)
    countrycode = models.CharField(db_column='countryCode', max_length=100)  # Field name made lowercase.
    budget = models.CharField(max_length=20)
    message = models.CharField(max_length=1000)
    attachment = models.CharField(max_length=1000)
    date = models.CharField(max_length=30)
    read_status = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'contact'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Faqs(models.Model):
    f_id_pk = models.BigAutoField(primary_key=True)
    faq_img = models.CharField(max_length=100)
    faq_heading = models.CharField(max_length=300)
    faq_one = models.CharField(max_length=1000)
    faq_two = models.CharField(max_length=1000)
    faq_three = models.CharField(max_length=1000)
    faq_four = models.CharField(max_length=1000)
    faq_five = models.CharField(max_length=1000)
    faq_six = models.CharField(max_length=1000)
    faq_ans_1 = models.CharField(max_length=1000)
    faq_ans_2 = models.CharField(max_length=1000)
    faq_ans_3 = models.CharField(max_length=1000)
    faq_ans_4 = models.CharField(max_length=1000)
    faq_ans_5 = models.CharField(max_length=1000)
    faq_ans_6 = models.CharField(max_length=1000)
    p_1_name = models.CharField(max_length=200)
    p_2_name = models.CharField(max_length=200)
    p_3_name = models.CharField(max_length=200)
    p_4_name = models.CharField(max_length=200)
    p_5_name = models.CharField(max_length=200)
    p_6_name = models.CharField(max_length=200)
    p_1_value = models.CharField(max_length=3)
    p_2_value = models.CharField(max_length=3)
    p_3_value = models.CharField(max_length=3)
    p_4_value = models.CharField(max_length=3)
    p_5_value = models.CharField(max_length=3)
    p_6_value = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'faqs'


class Projects(models.Model):
    p_id_pk = models.BigAutoField(primary_key=True)
    p_name = models.CharField(max_length=500)
    p_service = models.CharField(max_length=500)
    p_desc_1 = models.CharField(max_length=10000)
    p_desc_2 = models.CharField(max_length=10000)
    p_img_1 = models.CharField(max_length=100)
    p_img_2 = models.CharField(max_length=100)
    p_img_3 = models.CharField(max_length=100)
    p_img_4 = models.CharField(max_length=100)
    p_skill_1 = models.CharField(max_length=100)
    p_skill_2 = models.CharField(max_length=100)
    p_skill_3 = models.CharField(max_length=100)
    p_skill_4 = models.CharField(max_length=100)
    p_skill_5 = models.CharField(max_length=100)
    p_skill_6 = models.CharField(max_length=100)
    p_skill_7 = models.CharField(max_length=100)
    p_skill_8 = models.CharField(max_length=100)
    p_skill_9 = models.CharField(max_length=100)
    p_skill_10 = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'projects'


class Reviews(models.Model):
    r_id_pk = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    review = models.CharField(max_length=500)
    desg = models.CharField(max_length=100)
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'reviews'


class Services(models.Model):
    ser_id_pk = models.BigAutoField(primary_key=True)
    ser_name = models.CharField(max_length=100)
    ser_image = models.CharField(max_length=200)
    ser_header_img = models.CharField(max_length=200)
    ser_side_img = models.CharField(max_length=200)
    ser_desc_1 = models.CharField(max_length=10000)
    ser_desc_2 = models.CharField(max_length=10000)
    ser_one = models.CharField(max_length=500)
    ser_two = models.CharField(max_length=500)
    ser_three = models.CharField(max_length=500)
    ser_four = models.CharField(max_length=500)
    ser_five = models.CharField(max_length=500)
    ser_six = models.CharField(max_length=500)
    ser_seven = models.CharField(max_length=500)
    ser_eight = models.CharField(max_length=500)
    ser_nine = models.CharField(max_length=500)
    ser_ten = models.CharField(max_length=500)
    ser_eleven = models.CharField(max_length=500)
    ser_twelve = models.CharField(max_length=500)
    head_text = models.CharField(max_length=500)
    ser_url = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'services'


class Skills(models.Model):
    s_id_pk = models.BigAutoField(primary_key=True)
    skill_name = models.CharField(max_length=100)
    skill_image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'skills'


class User(models.Model):
    u_id_pk = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'users'

    def __str__(self):
        return self.username



