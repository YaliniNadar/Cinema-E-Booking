import this
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField
from .models import CustomUser, Address, PaymentCard


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    receive_promos = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = ("username", "email")

<<<<<<< HEAD
=======
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"
>>>>>>> d91c9392ecfee713befa11f632a9208191edbf3d

class PaymentForm(forms.ModelForm):
    cc_code = forms.CharField(
        widget=forms.PasswordInput(render_value=True),
        max_length=4,
        label="Security Code",
    )

    class Meta:
        model = PaymentCard
<<<<<<< HEAD
        exclude = ("card_id",)

=======
        exclude = ('card_id','card_owner','billing_address')
>>>>>>> d91c9392ecfee713befa11f632a9208191edbf3d

class SelectCardForm(forms.ModelForm):
    
    class Meta:
<<<<<<< HEAD
        model = Address
        fields = "__all__"
=======
        model = CustomUser
        fields = ("usercards",)
>>>>>>> d91c9392ecfee713befa11f632a9208191edbf3d
