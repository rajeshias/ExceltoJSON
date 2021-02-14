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

### Sometimes JSON has an empty list as value, we need to tell the program that this key has no values, but the value is a list. Or else the program puts "" instead of []. So we will be adding a separator in the key as a suffix to tell the program that this key is an exception
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
    <td>key2_</td>
    <td>value1</td>
    <td>value2</td>
    <td>value3</td>
  </tr>
  <tr>
    <td>key3_</td>
  </tr>
</table>
JSON format = { "key1":"value1" , "key2":["value1", "value2", "value3"] , "key3":[] }
