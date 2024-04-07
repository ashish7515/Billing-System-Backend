## API Documentation

If you're looking to interact with our system programmatically, all our API routes are accessible at [this link](https://billing-system-backend-tshx.onrender.com/api/schema/docs/).

### Managing Products
- Need to add, update, or remove products? Check out the Product Section for the right APIs to use.

### Managing Employees
- For tasks related to employees like adding new ones, updating their details, or removing them, head to the Employee Section.

### Billing Process
- To create a bill for a customer, follow these steps:
   1. Start by making an empty bill using the `POST /bills/` endpoint. This sets up the structure for the bill.
   2. Then, add the items the customer wants to purchase using `POST /bill-items`. This links the products to the bill.
   3. Finally, you can retrieve the bill for any customer by using the `GET /bills/` endpoint.

### Registering as an Employee
- If you're an employee, you'll first need to register on our application through `POST /api/login/`. This gives you access to perform tasks like creating bills, managing products, and handling customer details.
- After registering, grab the access token from the response and enter it into the authorize button on the top right corner of the application. This ensures you're recognized as an authorized employee.
- Once authorized, simply log in using your email and password.

### Additional Notes
- If you're adding a new customer, use `POST /api/customers/` to create their profile. If the customer is already registered, you can find them in our database using a simple GET request.
