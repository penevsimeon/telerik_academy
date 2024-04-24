<img src="https://i.imgur.com/yqIN5FX.png" width="300px" />

# Cosmetics shop - workshop (OOP - Classes exercise)

### 1. Description
The shop already has a working Engine. You do not have to touch anything in it. Just use it.
Each product has **name, brand, price and gender** (men, women, unisex).
There are **categories** of products. Each **category** has **name** and products can be **added or removed**. There is also a **shopping cart**. Products can be **added or removed** from it. The same product can be added to the shopping cart more than once. The shopping cart can calculate the **total price** of all products in it.
- Your **task** is to **finish the implementation** of the classes to model the cosmetics shop.
- The **NotImplementedErrors** should give you an idea where to write code.

### 2. Category class
#### Description
- Minimum category name’s length is 2 symbols and maximum is 15 symbols.
- `products` property getter should return an immutable collection (tuple)
- Products in category should be displayed in insertion order
- When removing product from category, if the product is not found you should raise an error.
- Category’s `to_string()` should return text in the following format:

```
#Category: {category name}
 #{Name} {Brand}
 #Price: ${price}
 #Gender: {genderType}
 ===
 #{Name} {Brand}
 #Price: ${price}
 #Gender: {genderType}
```

```
#Category: {category name}
 #No products in this category
```

### 3. Products
#### Description
- Minimum product name’s length is 3 symbols and maximum is 10 symbols.
- Minimum brand name’s length is 2 symbols and maximum is 10 symbols.
- Price cannot be negative.
- Gender type can be **"Men"**, **"Women"** or **"Unisex"**. (implemented)
- Print returns text in the following format: _(you might consider reusing this in the category print.)_
```
 #{Name} {Brand}
 #Price: ${Price}
 #Gender: {GenderType}
```
> Two products with **the same name** are considered equal. (rules for checking whether a product exists in a collection)

### 3. ApplicationData class
#### Description
- An instance of this class will hold all application data
- Attributes 
   - `products` (collection) 
   - `categories` (collection)
   -  `ShoppingCart`

- Methods
    - can create Category/Product. ValueError if category/product with the same name already exists
    - find - returns Category/Product. ValueError if a category/product with that name does not exist
    - exists - return bool for whether a product/category with the searched name exists

 

### 4. Shopping cart
#### Description
- Adding the same product more than once is allowed.
- Removing a product from the shopping cart does not throw an error
- The cart can calculate the total price of all products
- The cart can check if a product is currently added to it

> **Constraint 1** - If a null value is passed to some mandatory property, your program should raise a proper error.  
> **Constraint 2** - You should only write code in the classes in the models folder and the ApplicationData class

> **Notes** - To simplify your work you are given an already built Engine (for executing some basic operations) and Commands (handle the logic for different operations).

### Input example

```
CreateProduct MyMan Trashy 10.99 Men
CreateCategory Shampoos
AddToCategory Shampoos MyMan
AddToShoppingCart MyMan
ShowCategory Shampoos 
TotalPrice
RemoveFromCategory Shampoos MyMan
ShowCategory Shampoos
RemoveFromShoppingCart MyMan
TotalPrice
End
```

### Output Example

```
Product with name MyMan was created!
Category with name Shampoos was created!
Product MyMan added to category Shampoos!
Product MyMan was added to the shopping cart!
#Category: Shampoos
 #MyMan Trashy
 #Price: $10.99
 #Gender: Men
$10.99 total price currently in the shopping cart!
Product MyMan removed from category Shampoos!
#Category: Shampoos
 #No products in this category
Product MyMan was removed from the shopping cart!
No products in shopping cart!
```

> **Hint**: You don't need to take care of the Engine class, the CommandFactory class, the Main method, and the Commands but you can understand how they work

>You are given a template of the Cosmetics shop. Please take a look at it carefully before you try to do anything. Try to understand all the classes and how they are supposed to interact with each other.

### Unit Tests

- You have been given unit tests to keep track off your progress. Run them from the Testing explorer in the nav menu in VSCode
- Should you get stuck, check out the tests' names to guide you what you should do.

## Step by step guide

> *Hint: Run the tests whenever you finish a task to check if it's implemented correctly.*

1. Start with the `Product` class
   - Apply the Encapsulation principle to all the attributes (make sure all fields are private (by convention), add provide properties for them).

1. Navigate to the `ApplicationData` class

    - Implement the `find` methods - they should go through the respective collections and return the item that has the given name. What should happen if there is no item with that name? Maybe throw an exception?
    - Implement the `create` methods - they accept the needed arguments to create a category or a product.
    - Implement the `exists` methods - they go through the respective collections and return `true` if there is an item that has the given name.

1. Finish the `ShoppingCart` class

    - Encapsulate it (don't allow direct access to it).
    - Initialize the `products` collection.

    ```python
    def __init__(self):
        self._products = []
    ```

    - Implement the methods that add or remove products from the collection.

1. Finish the `Category` class

   - Initialize the collection.
   - Implement the methods that add or remove products from the collection.

1. Implement `to_string()` methods in both the `Category` and `Product` classes.

   - To test the `to_string()` method you need to run the application, pass the sample input and check the output.
   - There is also a unit test for the `product.to_string()` which you can use

