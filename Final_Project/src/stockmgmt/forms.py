from django import forms
from .models import *
from .models import *


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("This field is required. Please enter something.")
        return name



class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name', 'quantity']
     
    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError('This field is required')
        # for instance in Stock.objects.all():
        #     if instance.category == category:
        #         raise forms.ValidationError(str(category) + ' is already created')
        return category

    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if not item_name:
          raise forms.ValidationError('This field is required')

        # Check if the item_name already exists in the database
        if Stock.objects.filter(item_name__iexact=item_name).exists():
            raise forms.ValidationError(str(item_name) + ' is already added')

        return item_name

class StockSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Stock
        fields = ['category', 'item_name']


class StockUpdateForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['category', 'item_name', 'quantity']



# class IssueForm(forms.ModelForm):
#     class Meta:
#         model = Stock
#         fields = ['issue_quantity', 'issue_to']

#     def clean_issue_quantity(self):
#         issue_quantity = self.cleaned_data.get('issue_quantity')
#         if issue_quantity <= 0:
#             raise forms.ValidationError("Please enter a number greater than zero.")
#         return issue_quantity


class IssueForm(forms.ModelForm):
    issue_to = forms.CharField(max_length=255, required=False)

    class Meta:
        model = Stock
        fields = ['issue_quantity', 'issue_to']

    def clean_issue_quantity(self):
        issue_quantity = self.cleaned_data.get('issue_quantity')
        if issue_quantity <= 0:
            raise forms.ValidationError("Please enter a number greater than zero.")
        return issue_quantity

    def clean(self):
        cleaned_data = super().clean()
        issue_to = cleaned_data.get('issue_to')
        if not issue_to:
            raise forms.ValidationError("Please enter the name of the person/organization you want to supply the item to.")
        return cleaned_data




class ReceiveForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['receive_quantity']

    def clean_receive_quantity(self):
        receive_quantity = self.cleaned_data.get('receive_quantity')
        if receive_quantity <= 0:
            raise forms.ValidationError("Please enter a number greater than zero.")
        return receive_quantity








# Invoice Start


# class InvoiceForm(forms.ModelForm):
# 	class Meta:
# 		model = Invoice
# 		fields = ['name', 'phone_number', 'invoice_date', 'invoice_number',
# 				'line_one', 'line_one_quantity', 'line_one_unit_price', 'line_one_total_price',
# 				'line_two', 'line_two_quantity', 'line_two_unit_price', 'line_two_total_price',
# 				'line_three', 'line_three_quantity', 'line_three_unit_price', 'line_three_total_price',
# 				'line_four', 'line_four_quantity', 'line_four_unit_price', 'line_four_total_price',
# 				'line_five', 'line_five_quantity', 'line_five_unit_price', 'line_five_total_price', 
# 				'total', 'paid', 'invoice_type'
# 				]


class InvoiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['name', 'phone_number', 'invoice_date', 'invoice_number',
                  'line_one', 'line_one_quantity', 'line_one_unit_price', 'line_one_total_price',
                  'line_two', 'line_two_quantity', 'line_two_unit_price', 'line_two_total_price',
                  'line_three', 'line_three_quantity', 'line_three_unit_price', 'line_three_total_price',
                  'line_four', 'line_four_quantity', 'line_four_unit_price', 'line_four_total_price',
                  'line_five', 'line_five_quantity', 'line_five_unit_price', 'line_five_total_price',

                  'line_six', 'line_six_quantity', 'line_six_unit_price', 'line_six_total_price',
				'line_seven', 'line_seven_quantity', 'line_seven_unit_price', 'line_seven_total_price',
				'line_eight', 'line_eight_quantity', 'line_eight_unit_price', 'line_eight_total_price',
				'line_nine', 'line_nine_quantity', 'line_nine_unit_price', 'line_nine_total_price',
				'line_ten', 'line_ten_quantity', 'line_ten_unit_price', 'line_ten_total_price', 
                  'total_quantity', 'paid', 'invoice_type']  # Include the required fields in the form





class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['name', 'phone_number', 'invoice_date', 'invoice_number',
                  'line_one', 'line_one_quantity', 'line_one_unit_price', 'line_one_total_price',
                  'line_two', 'line_two_quantity', 'line_two_unit_price', 'line_two_total_price',
                  'line_three', 'line_three_quantity', 'line_three_unit_price', 'line_three_total_price',
                  'line_four', 'line_four_quantity', 'line_four_unit_price', 'line_four_total_price',
                  'line_five', 'line_five_quantity', 'line_five_unit_price', 'line_five_total_price', 

                  'line_six', 'line_six_quantity', 'line_six_unit_price', 'line_six_total_price',
				'line_seven', 'line_seven_quantity', 'line_seven_unit_price', 'line_seven_total_price',
				'line_eight', 'line_eight_quantity', 'line_eight_unit_price', 'line_eight_total_price',
				'line_nine', 'line_nine_quantity', 'line_nine_unit_price', 'line_nine_total_price',
				'line_ten', 'line_ten_quantity', 'line_ten_unit_price', 'line_ten_total_price',
                  'total_quantity', 'paid', 'invoice_type']


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['name', 'phone_number', 'invoice_date', 'invoice_number',
                  'line_one', 'line_one_quantity', 'line_one_unit_price', 'line_one_total_price',
                  'line_two', 'line_two_quantity', 'line_two_unit_price', 'line_two_total_price',
                  'line_three', 'line_three_quantity', 'line_three_unit_price', 'line_three_total_price',
                  'line_four', 'line_four_quantity', 'line_four_unit_price', 'line_four_total_price',
                  'line_five', 'line_five_quantity', 'line_five_unit_price', 'line_five_total_price', 

                  'line_six', 'line_six_quantity', 'line_six_unit_price',
                  'line_six_total_price',
				'line_seven', 'line_seven_quantity', 'line_seven_unit_price', 'line_seven_total_price',
				'line_eight', 'line_eight_quantity', 'line_eight_unit_price', 'line_eight_total_price',
				'line_nine', 'line_nine_quantity', 'line_nine_unit_price', 'line_nine_total_price',
				'line_ten', 'line_ten_quantity', 'line_ten_unit_price', 'line_ten_total_price',
                  'total_quantity', 'paid', 'invoice_type']
    
         # Add Bootstrap classes manually to the widgets
        widgets = {
            'invoice_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            # Add other fields here if needed
        }



    def clean_invoice_number(self):
        invoice_number = self.cleaned_data.get('invoice_number')
        if not invoice_number:
            raise forms.ValidationError('This field is required')

        # Check if the invoice_number is negative
        if invoice_number < 0:
            raise forms.ValidationError("Invoice number cannot be negative.")

        # Check if the invoice_number already exists
        if Invoice.objects.filter(invoice_number=invoice_number).exists():
            raise forms.ValidationError("Invoice number already exists. Please enter a different number.")

        return invoice_number


    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')
        return name

    def clean_line_one(self):
        line_one = self.cleaned_data.get('line_one')
        if not line_one:
            raise forms.ValidationError('This field is required')
        return line_one


    def clean_line_one_quantity(self):
        line_one_quantity = self.cleaned_data.get('line_one_quantity')
        if not line_one_quantity:
            raise forms.ValidationError('This field is required')

        if line_one_quantity < 0:
            raise forms.ValidationError("Please enter a number greater than zero.")
        return line_one_quantity

    def clean_line_two_quantity(self):
        line_two_quantity = self.cleaned_data.get('line_two_quantity')
        if line_two_quantity < 0:
            raise forms.ValidationError("Please enter a number greater than zero.")
        return line_two_quantity

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

        # Check if phone_number contains only digits
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number  must contain only digits.")

        # Check if phone_number is either 9 or 12 digits long
        if len(phone_number) not in [9, 12]:
            raise forms.ValidationError("Please enter correct phone number.")

        # Check if phone_number is a non-negative number
        if int(phone_number) < 0:
            raise forms.ValidationError("Phone number cannot be negative.")

        return phone_number

    # Add similar clean methods for other quantity fields if needed

class InvoiceSearchForm(forms.ModelForm):
    generate_invoice = forms.BooleanField(required=False)

    class Meta:
        model = Invoice
        fields = ['invoice_number', 'name', 'generate_invoice']

class ReorderLevelForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['reorder_level']




# Invoice end