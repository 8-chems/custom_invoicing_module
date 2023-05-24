This project was written to satisfy recruiter specification described below:
----------------------------------
Using Odoo Community Edition v16 create a custom app that has the following features:

1. Metal price table: In the invoicing app (tree view), add a new menu next to "Vendor" that opens a wizard that has a table that takes a daily "Metal price" and current date "Date". It should display historical data from previous days. "Date" should by default show the current date but it could be edited.

2. In invoice form view:

   a. Add a field that shows today's "metal price" (if it was added in the wizard). If it wasn't added previously the user can enter it from this field and it'll be saved along with the current date and it should appear in the metal price table. The field should be placed after "partner_id" field.
   
   b. Make account move line "total" field editable for products that has a UoM of type "weight" only. 
     - When a value is entered in "total" the tax needs to be subtracted from the value entered then the result, which is "price_subtotal", will be divided by "quantity" to calculate "price_unit". The regular calculation should still work as well. Also, make sure the value entered in the "total" field doesn't change. 
     - "Quantity" should be required. Show an alert message if a value is entered in "total" while "quantity" is empty.

3. In the customer (partner) form view add a smart button that displays the total of "quantity" column billed to that customer that has UoM of type "weight". Behaves similar to the "invoiced" button so it should show the invoices when you click on it. Only invoices that has lines with UoM of type "weight" should appear.

Units of measure of type "weight": "g", "kg", "lb" etc.