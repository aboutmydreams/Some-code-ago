<<?php  ?>
<?php
echo '你的姓名是:'.$_POST['name'];//其中$_POST['name']中存放的是上面表单名为name的-=值
echo '你今年'.$_POST['age'].'岁';//其中$_POST['age']中存放的是上面表单名为age的值
?>
<form method="post">
    <p>姓名:<input type="text" name="name" value=""></p>
    <p>年龄:<input type="text" name="age" value=""></p>
    <p><input type="submit" value="提交"></p>
</form>