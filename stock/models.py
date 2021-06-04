from django.db import models
from django.db.models import Max

# ?  Work through this model and comment where relationships exist and note the type.
class Stock(models.Model):

<<<<<<< HEAD
    def number_of_stock_items():
=======
    def stock_num_index():
>>>>>>> main
        stock = Stock.objects.all()
        num = stock.aggregate(Max('stock_num'))['stock_num__max']
        if num is None:
            return 1
        else:
            return num + 1


    stock_type = models.CharField(max_length=1, blank=True, null=True)
<<<<<<< HEAD
    stock_num = models.IntegerField(default=number_of_stock_items, blank=True, null=True)   
=======
    stock_num = models.IntegerField(default=stock_num_index, blank=True, null=True)   
>>>>>>> main
    stock_code = models.CharField(primary_key=True, max_length=20)
    partnership = models.BooleanField(blank=True, null=True)
    status = models.CharField(blank=True, null=True, max_length=20)
    # category_id = models.IntegerField(blank=True, null=True)
    category_id = models.ForeignKey(
        'categories.Category', 
        on_delete=models.CASCADE, 
        related_name="category",
        blank=True, 
        null=True, 
        db_column='category_id'
    )
    # sub_category_1_id = models.IntegerField(blank=True, null=True)
    sub_category_1_id = models.ForeignKey(
        'categories.Category', 
        on_delete=models.CASCADE,
        related_name="sub_category_1", 
        blank=True, 
        null=True, 
        db_column='sub_category_1_id'
    )
    # sub_category_2_id = models.IntegerField(blank=True, null=True)
    sub_category_2_id = models.ForeignKey(
        'categories.Category', 
        on_delete=models.CASCADE, 
        related_name="sub_category_2",
        blank=True, 
        null=True, 
        db_column='sub_category_2_id'
    )
<<<<<<< HEAD

    # category_id = models.OneToOneField(
    #     'categories.Category', 
    #     on_delete=models.CASCADE, 
    #     related_name="category",
    #     blank=True, 
    #     null=True, 
    #     db_column='category_id'
    # )
    # sub_category_1_id = models.OneToOneField(
    #     'categories.Category', 
    #     on_delete=models.CASCADE,
    #     related_name="sub_category_1", 
    #     blank=True, 
    #     null=True, 
    #     db_column='sub_category_1_id'
    # )
    # sub_category_2_id = models.OneToOneField(
    #     'categories.Category', 
    #     on_delete=models.CASCADE, 
    #     related_name="sub_category_2",
    #     blank=True, 
    #     null=True, 
    #     db_column='sub_category_2_id'
    # )
=======
>>>>>>> main
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # artist_id = models.IntegerField(blank=True, null=True)
    artist_id = models.ForeignKey(
        'names.Name', 
        on_delete=models.CASCADE, 
        related_name="artist_stock",
        blank=True, 
        null=True, 
        db_column='artist_id'
    )
    item_date = models.CharField(max_length=100, blank=True, null=True)
    provenance = models.CharField(max_length=100, blank=True, null=True)
    published = models.TextField(blank=True, null=True)
    exhibited = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    missing_info = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    # location_id = models.IntegerField(blank=True, null=True)
    location_id = models.ForeignKey(
        'names.Name', 
        on_delete=models.CASCADE, 
        related_name="location_stock",
        blank=True, 
        null=True, 
        db_column='location_id'
    )
    location_notes = models.TextField(blank=True, null=True)
    acquisition_date = models.DateTimeField(blank=True, null=True)
    # source_id = models.IntegerField(blank=True, null=True)
    source_id = models.ForeignKey(
        'names.Name', 
        on_delete=models.CASCADE, 
        related_name="source_stock",
        blank=True, 
        null=True,
        db_column='source_id'
    )
    source_lot_number = models.TextField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    length_notes = models.TextField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    width_notes = models.TextField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    height_notes = models.TextField(blank=True, null=True)
    diameter = models.FloatField(blank=True, null=True)
    diameter_notes = models.TextField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    weight_notes = models.TextField(blank=True, null=True)
    needs_measuring = models.BooleanField(blank=True, null=True)
    trany = models.BooleanField(blank=True, null=True)
    low_res_scan = models.BooleanField(blank=True, null=True)
    high_res_scan = models.BooleanField(blank=True, null=True)
    colour_print = models.BooleanField(blank=True, null=True)
    colour_negative = models.BooleanField(blank=True, null=True)
    bw_print = models.BooleanField(blank=True, null=True)
    bw_negative = models.BooleanField(blank=True, null=True)
    photo_ref = models.TextField(blank=True, null=True)
    image_address = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    commission_notes = models.TextField(blank=True, null=True)
    quote_modified_date = models.DateTimeField(blank=True, null=True)
    acc_min_ask_price = models.FloatField(blank=True, null=True)
    quote_min_ask_price = models.FloatField(blank=True, null=True)
    acc_max_ask_price = models.FloatField(blank=True, null=True)
    quote_max_ask_price = models.FloatField(blank=True, null=True)
    acc_est_sell_price = models.FloatField(blank=True, null=True)
    quote_est_sell_price = models.FloatField(blank=True, null=True)
    quote_rate = models.FloatField(blank=True, null=True)
    quote_currency = models.TextField(blank=True, null=True)
    consignee = models.TextField(blank=True, null=True)
    acc_activities_cost = models.FloatField(blank=True, null=True)
    sensitive_acquisition = models.BooleanField(blank=True, null=True)
    purchase_invoice_number = models.TextField(blank=True, null=True)
    sale_invoice_number = models.TextField(blank=True, null=True)
    partner_purchase_invoice_number = models.TextField(blank=True, null=True)
    partner_sale_invoice_number = models.TextField(blank=True, null=True)
    consignment_date = models.DateTimeField(blank=True, null=True)
    consignor_valuation_currency = models.TextField(blank=True, null=True)
    acc_consignor_valuation_amount = models.FloatField(blank=True, null=True)
    und_consignor_valuation_amount = models.FloatField(blank=True, null=True)
    consignor_valuation_pay_rate = models.FloatField(blank=True, null=True)
    disposal_date = models.DateTimeField(blank=True, null=True)
    # buyer_id = models.IntegerField(blank=True, null=True)
    buyer_id = models.ForeignKey(
        'names.Name', 
        on_delete=models.CASCADE, 
        related_name="buyer_stock",
        blank=True, 
        null=True,
        db_column='buyer_id'
    )
    buyer_lot_number = models.TextField(blank=True, null=True)
    returned_to_consignor = models.BooleanField(blank=True, null=True)
    # partner_id = models.IntegerField(blank=True, null=True)
    partner_id = models.ForeignKey(
        'names.Name', 
        on_delete=models.CASCADE, 
        related_name="partner_stock",
        blank=True, 
        null=True,
        db_column='partner_id'
    )
    partner_acquisition_pay_method = models.TextField(blank=True, null=True)
    partner_disposal_pay_method = models.TextField(blank=True, null=True)
    acquisition_pay_method = models.TextField(blank=True, null=True)
    disposal_pay_method = models.TextField(blank=True, null=True)
    acquisition_pay_rate = models.FloatField(blank=True, null=True)
    disposal_pay_rate = models.FloatField(blank=True, null=True)
    vat_arrangement = models.IntegerField(blank=True, null=True)
    partner_arrangement = models.IntegerField(blank=True, null=True)
    margin_arrangement = models.IntegerField(blank=True, null=True)
    acquisition_currency = models.TextField(blank=True, null=True)
    disposal_currency = models.TextField(blank=True, null=True)
    disposal_vat_type = models.TextField(blank=True, null=True)
    acquisition_vat_rate = models.FloatField(blank=True, null=True)
    disposal_vat_rate = models.FloatField(blank=True, null=True)
    commission_percentage = models.FloatField(blank=True, null=True)
    partner_acquisition_percentage = models.FloatField(blank=True, null=True)
    partner_sale_percentage = models.FloatField(blank=True, null=True)
    acc_gross_cost = models.FloatField(blank=True, null=True)
    und_gross_cost = models.FloatField(blank=True, null=True)
    acc_gross_sale = models.FloatField(blank=True, null=True)
    und_gross_sale = models.FloatField(blank=True, null=True)
    acc_partner_cost = models.FloatField(blank=True, null=True)
    und_partner_cost = models.FloatField(blank=True, null=True)
    acc_partner_sale = models.FloatField(blank=True, null=True)
    und_partner_sale = models.FloatField(blank=True, null=True)
    acc_net_cost = models.FloatField(blank=True, null=True)
    und_net_cost = models.FloatField(blank=True, null=True)
    acc_net_sale = models.FloatField(blank=True, null=True)
    und_net_sale = models.FloatField(blank=True, null=True)
    acc_acquisition_vat = models.FloatField(blank=True, null=True)
    und_acquisition_vat = models.FloatField(blank=True, null=True)
    acc_disposal_vat = models.FloatField(blank=True, null=True)
    und_disposal_vat = models.FloatField(blank=True, null=True)
    acc_commission_vat = models.FloatField(blank=True, null=True)
    und_commission_vat = models.FloatField(blank=True, null=True)
    acc_outside_commission = models.FloatField(blank=True, null=True)
    und_outside_commission = models.FloatField(blank=True, null=True)
    acc_gross_cost_minus_vat = models.FloatField(blank=True, null=True)
    und_gross_cost_minus_vat = models.FloatField(blank=True, null=True)
    acc_gross_sale_minus_vat = models.FloatField(blank=True, null=True)
    und_gross_sale_minus_vat = models.FloatField(blank=True, null=True)
    acc_gross_margin = models.FloatField(blank=True, null=True)
    und_gross_margin = models.FloatField(blank=True, null=True)
    acc_net_margin = models.FloatField(blank=True, null=True)
    und_net_margin = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'stock'

    def __str__(self):
        return f"{self.stock_code} - {self.title}"