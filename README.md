# assignment_2

List all the product items on web page.

```
https://assignment.pythonanywhere.com
```


# Rest api
## | For retrive all the products details
```
https://assignment.pythonanywhere.com
```
## | For retrive the products details specificly with slug of the product

```
 https://assignment.pythonanywhere.com/api/products/example-slug-title/
```
## | Delete product data from database with ID.

```
https://assignment.pythonanywhere.com/api/products/1/
```
## | To add product to the database use .
```
https://assignment.pythonanywhere.com/api/products/
```
body format in ```JSON```
~~~
{ 
    "slug" : "auto-slug-field",
    "product_name" : "product name",
    "discription" : "product detail",        
    "price" : 100.00,
    "product_img" : "image url"                                                                                                       
}
~~~

## | If you want to update any field's existing product detail you can use . 

```
https://assignment.pythonanywhere.com/api/products/1/
```
```
{ 
    "slug" : "auto-slug-field",
    "product_name" : "...",
    "discription" : "...",        
    "price" : ...,
    "product_img" : "..."
}
```
## | If you want to update all the fields data once use this . 
```
{ 
    "slug" : "auto-slug-field",
    "product_name" : "...",
    "discription" : "...",        
    "price" : ...,
    "product_img" : "..."                                                                                                       
}

````
