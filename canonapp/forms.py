from django import forms

from .models import *




class CarForm(forms.ModelForm):

    class Meta:

        model=Car

        fields=('car_name','car_model','car_engine_no','car_registration_no',

              'car_consumption_rate','car_image')





class ComplaintsForm(forms.ModelForm):

    class Meta:

        model=Complaints

        fields=('complaint','complainant','other_complainant')







class DriverForm(forms.ModelForm):

    class Meta:

        model=Driver

        fields=('driver_name','driver_next_of_kin','driver_next_of_kin_contact','next_of_kin_national_id_image','driver_licence_no',

                'driver_contact','driver_email','driver_image','driver_monthly_payment','driver_permit_or_nationalID_image','attached_car')






class DriverPaymentForm(forms.ModelForm):

    class Meta:

        model=DriverPayment

        fields=('date','driver_name','paid_amount','paid_by','received_by')


class DriverCheckListForm(forms.ModelForm):
    class Meta:
        model=Driver_checklist

        fields=('date','driver_name','checklist_file')







#accountant forms start



class SpendForm(forms.ModelForm):

    class Meta:

        model=Spend

        fields=('Date','PaymentMadeTo','ReasonForPayment','Amount','AmountInWords', 'ReceivedBy', 'ApprovedBy')



class SundryForm(forms.ModelForm):

    class Meta:

        model=Sundry

        fields=('Date','PaymentMadeTo','ReasonForPayment','Amount','AmountInWords')



class SalaryForm(forms.ModelForm):

    class Meta:

        model=Salary

        fields = ('Date','Staff','Salary_Type','Month','Amount','AmountInWords')

#accountant add church Member
class AddChurchMemberForm(forms.ModelForm):

    class Meta:

        model=ChurchMember

        fields = ('Name','Address','Occupation','Status','Genda','Contact')
