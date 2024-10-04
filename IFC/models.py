# myapp/models.py

from django.db import models

"""
EXAMPLE OF HOW TO MAKE A TABLE:
class table_name(models.Model):
    name = models.CharField(max_length=100)   # This creates a VARCHAR column
    age = models.IntegerField()               # This creates an INTEGER column
    price = models.DecimalField(max_digits=10, decimal_places=2) # This creates a DECIMAL column

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'table_table'   # Explicitly set the table name
"""

class Acacia(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Acacia'

class Alpha_Chi_Rho(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Alpha_Chi_Rho'

class Alpha_Epsilon_Pi(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Alpha_Epsilon_Pi'

class Alpha_Sigma_Phi(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Alpha_Sigma_Phi'

class Chi_Phi(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Chi_Phi'

class Delta_Kappa_Epsilon(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Delta_Kappa_Epsilon'

class Delta_Phi(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Delta_Phi'

class Lambda_Chi_Alpha(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Lambda_Chi_Alpha'

class Phi_Gamma_Delta(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Phi_Gamma_Delta'

class Phi_Kappa_Theta(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'hi_Kappa_Theta'

class Phi_Mu_Delta(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Phi_Mu_Delta'

class Phi_Sigma_Kappa(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Phi_Sigma_Kappa'

class Pi_Kappa_Alpha(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Pi_Kappa_Alpha'

class Pi_Lambda_Phi(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Pi_Lambda_Phi'

class Psi_Upsilon(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Psi_Upsilon'

class Sigma_Alpha_Epsilon(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Sigma_Alpha_Epsilon'

class Sigma_Chi(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Sigma_Chi'

class Sigma_Phi_Epsilon(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Sigma_Phi_Epsilon'

class Tau_Epsilon_Phi(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Tau_Epsilon_Phi'

class Tau_Kappa_Epsilon(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Tau_Kappa_Epsilon'

class Theta_Xi(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Theta_Xi'

class Zeta_Psi(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Zeta_Psi'

class Delta_Tau_Delta(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Delta_Tau_Delta'

class Alpha_Phi_Alpha(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Alpha_Phi_Alpha'

class Phi_Iota_Alpha(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Phi_Iota_Alpha'

class Pi_Delta_Psi(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Pi_Delta_Psi'

class Lambda_Upsilon_Lambda(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Lambda_Upsilon_Lambda'

class Omega_Phi_Beta(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Omega_Phi_Beta'

class Sigma_Iota_Alpha(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Sigma_Iota_Alpha'

class Alpha_Gamma_Delta(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Alpha_Gamma_Delta'

class Alpha_Phi(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Alpha_Phi'

class Pi_Beta_Phi(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Pi_Beta_Phi'

class Alpha_Omega_Epsilon(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Alpha_Omega_Epsilon'

class Rensselaer_Society_Of_Engineering_Innovation(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Rensselaer_Society_Of_Engineering_Innovation'

class Order_Of_Omega(models.Model):
    nickname = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    member_count = models.IntegerField()
    president_name = models.CharField(max_length=100)
    president_phone_number = models.IntegerField()
    president_email = models.EmailField()
    primary_recruitment_chair_name = models.CharField(max_length=100)
    primary_recruitment_chair_phone_number = models.IntegerField()
    primary_recruitment_chair_email = models.EmailField()
    secondary_recruitment_chair_name = models.CharField(max_length=100)
    secondary_recruitment_chair_phone_number = models.IntegerField()
    secondary_recruitment_chair_email = models.EmailField()
    info_blurb = models.CharField(max_length=1000)
    founding_date = models.CharField(max_length=100)
    house_address = models.CharField(max_length=100)
    website_url = models.URLField(max_length=200) 
    instagram_url = models.URLField(max_length=200) 
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Order_Of_Omega'