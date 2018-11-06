function saveStorage() {//创建一个js对象用于存放信息
	var data = new Object;//将对象的属性值域用户输入联系起来
	data.user=document.getElementByid('user').value;
	data.mail=document.getElementByid('mail')value;
	data.tel=document.getElementByTid('tel').value;

	var str=JSON.stringify(data);//
	localStorage.setItem(data.user,str);
	console.log("数据已保存！用户为:"+data.user);

}
function findStorage(id){
	var requiredPersonName=document.getElementByid('find');
	var str=localStorage.getElem(requiredPersonName);
	var data=JSON.parse(str);
	var result="NAME:"+data.user+'<br>';
	result+="E-mail"+data.mail+'<br>';
	result+="Telphone"+data.tel+'<br>';
	var target=document.getElementByid('id');
	target.innerHTML =result;
}