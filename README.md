# ExceltoJSON
Converts Excel file containing json data into a JSON file
## Excel Format
Each key will be in the First Column, and each value data will be in the succeeding columns
<table style="width:100%">
  <tr>
    <th>keys</th>
    <th>values</th>
  </tr>
  <tr>
    <td>key1</td>
    <td>value1</td>
  </tr>
  <tr>
    <td>key2</td>
    <td>value1</td>
  </tr>
  <tr>
    <td>key3</td>
  </tr>
</table>
JSON format= { "key1":"value1" , "key2":"value1" , "key3":"" }

### What if the value is a list? <br>
Here we will be placing each element in the list(value) on each cell to the right of the key cell
<table style="width:100%">
  <tr>
    <th>keys</th>
    <th>values</th>
  </tr>
  <tr>
    <td>key1</td>
    <td>value1</td>
  </tr>
  <tr>
    <td>key2</td>
    <td>value1</td>
    <td>value2</td>
    <td>value3</td>
  </tr>
  <tr>
    <td>key3</td>
  </tr>
</table>
JSON format = { "key1":"value1" , "key2":["value1", "value2", "value3"] , "key3":"" }

Sometimes JSON has an empty list as value, we need to tell the program that this key has no values, but the value is a list. Or else the program puts "" instead of [].<br>
So we will be adding a separator (here '_') in the key as a suffix to tell the program that this key is an exception
<table style="width:100%">
  <tr>
    <th>keys</th>
    <th>values</th>
  </tr>
  <tr>
    <td>key1</td>
    <td>value1</td>
  </tr>
  <tr>
    <td>key2</td>
    <td>value1</td>
    <td>value2</td>
    <td>value3</td>
  </tr>
  <tr>
    <td>key3_</td>
  </tr>
</table>
JSON format = { "key1":"value1" , "key2":["value1", "value2", "value3"] , "key3":[] }


### Dealing with a dictionary inside a list as a value
If key3 has 3 other attributes like name,id,address. then the json file will have a dictionary of keys(name,id,address) inside a list as a value. To deal with this we will use a separator and distribute the attribute row wise (key3_name, key3_id, key3_address)
<table style="width:100%">
  <tr>
    <th>keys</th>
    <th>values</th>
  </tr>
  <tr>
    <td>key1</td>
    <td>value1</td>
  </tr>
  <tr>
    <td>key2</td>
    <td>value1</td>
    <td>value2</td>
    <td>value3</td>
  </tr>
  <tr>
    <td>key3_name</td>
    <td>Rajesh</td>
  </tr>
  <tr>
    <td>key3_id</td>
    <td>3027</td>
  </tr>
  <tr>
    <td>key3_address</td>
    <td>Dubai main rd</td>
    <td>Dubai bustand</td>
    <td>Dubai</td>
  </tr>
</table>
JSON format = { "key1":"value1" , "key2":["value1", "value2", "value3"] , "key3":[ { "name":"Rajesh", "id":3027, "address":["Dubai main rd", "Dubai bustand", "Dubai"] } ] }

## <u>note:</u>
notice how 3027 is not a string format<br>
Values will be unchanged, As excel supports int, str, and bool. The same DataType will be in JSON


# REQUIREMENTS:

<li>Pandas</li>
<li>json</li>

more details in requirements.txt

