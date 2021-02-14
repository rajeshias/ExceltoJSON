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
    <td>value1</td>
    <tf>value2</td>
  </tr>
</table>

What if the value is a list? <br>
Here we are adding a separator in the py code, that tells the program that this key is an exception! <br>
if the separator is '_' , then we will be placing each element in the list(value) on each cell to the right
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
    <td>key3</td>
    <td>value1</td>
  </tr>
</table>
