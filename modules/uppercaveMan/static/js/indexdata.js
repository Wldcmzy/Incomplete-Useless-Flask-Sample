window.console = window.console || (function(){ 
var c = {}; c.log = c.warn = c.debug = c.info = c.error = c.time = c.dir = c.profile = c.clear = c.exception = c.trace = c.assert = function(){}; 
return c; 
})(); 
//定义全局历史数据数组
//var arrlastData01 = new Array(50, 50, 50, 50, 50, 50, 50);　
//var arrlastData01 = [30, 40, 50, 60, 70, 80, 90];
var arrlastData01 = [];//风速
var arrlastData02 = [];//降雨
var arrlastData03 = [];//大气压
var arrlastData04 = [];//紫外线
var arrlastData05 = [];//总辐射
var arrlastData06 = [];//二氧化碳
var arrlastData07 = [];//湿度
var arrlastData08 = [];//光照度
var arrlastData09 = [];//地面温度
var arrlastData10 = [];//躁声
var arrlastData11 = [];//温度
var arrlastData12 = [];//风向
var arrlastData13 = [];//粉尘
function readData(isAppend, selector, url, data) {
	
	var lastId = null;
	$.ajax({
		url : url,
		dataType : 'json',
		data: data,
		async : false,
		success: function(data) {
			//console.log(data);
			if (!isAppend) $(selector).html('');
			
			if (data == null) {
				return;
			}
			
			if (!$.isArray(data)) {
				data = [data];
			}
			
			if (isAppend) {
				$(selector).append(getRowHtml(data));
			} else {
				$(selector).html(getRowHtml(data));
			}
			
			lastId = data[data.length - 1].id;
		}
	});
	
	return lastId;
}

function getRowHtml(data) {
	var row;
	var rHtml = [];
	
	
	for (var i = 0; i < data.length; i++) {
		row = data[i];
		
	    if (row.probe1 == "-10,000") {
			row.probe1= "无数据";	
			}		
	    if (row.probe2 == "-10,000") {
			row.probe2= "无数据";	
			}			
	    if (row.probe3 == "-10,000") {
			row.probe3= "无数据";	
			}		
	    if (row.probe4 == "-10,000") {
			row.probe4= "无数据";	
			}			
	    if (row.probe5 == "-10,000") {
			row.probe5= "无数据";	
			}		
	    if (row.probe6 == "-10,000") {
			row.probe6= "无数据";	
			}			
	    if (row.probe7 == "-10,000") {
			row.probe7= "无数据";	
			}		
	    if (row.probe8 == "-10,000") {
			row.probe8= "无数据";	
			}	
	    if (row.probe9 == "-10,000") {
			row.probe9= "无数据";	
			}		
	    if (row.probe10 == "-10,000") {
			row.probe10= "无数据";	
			}			
	    if (row.probe11 == "-10,000") {
			row.probe11= "无数据";	
			}		
	    if (row.probe15 == "-10000") {
			row.probe15= "无数据";
                        var Ndu = 31.21909;
                        var Edu = 121.403737;
			}		

        else if (row.probe15 == "NN  EE") {
			row.probe15= "暂无数据";
                        var Ndu = 31.390898;
                        var Edu = 120.986483;	
			}
        else		
		{
		// GPS显示的经度和纬度分开两行显示
		var gpsn = '';
		var gpse = '';
		if (row.probe15 != null) {
			gpsn = row.probe15.split(" ")[0];	
			gpse = row.probe15.split(" ")[2];
		}  
        //alert("纬度="+gpsn);  
	    //alert("经度="+gpse);		
		//纬度 度分秒格式转换开始
        var Nstr1 = gpsn.split("°");
		var Ndu = Nstr1[0];
		var Ntp = Nstr1[1].split("'");
		var Nfen = Ntp[0];
        var Nmiao = Ntp[1];
		var Nm = null;
		if(Nmiao!= null){ 
		//javascript中的获得字符串长度的方法是length  JAVA中的是length() 不能混用 这里有2处用到了length
	       var miao = Nmiao.substring(0,Nmiao.length-1);//去掉N、S   
		   if(miao.length == 0){
			  miao="0"; 
			  Nm = parseFloat(miao);
			  //alert("miao="+Nm); 调试数据
			}
			else{
			  Nm = parseFloat(miao);	
			}
		}
		//纬度格式转换结束
		
        //经度格式转换开始             
		var Estr1 = gpse.split("°");
		var Edu = Estr1[0];
		var Etp = Estr1[1].split("'");
		var Efen = Etp[0];
        var Emiao = Etp[1];
        var Em= null;
		if(Emiao!= null){   
		   var miao = Emiao.substring(0,Emiao.length-1);//去掉W、E
		   if(miao.length == 0){
			  miao="0"; 
			  Em = parseFloat(miao);
			}
			else{
			  Em = parseFloat(miao);	
			}
		}
		//经度格式转换结束		
		
		//计算总的纬度度数	
        var Nd = parseFloat(Ndu);
		var Nf = parseFloat(Nfen);
		var latitude = Nd + Nf/60 + Nm/3600;
        //("纬度="+latitude);
		
		//计算总的经度度数 
		var Ed = parseFloat(Edu);
		var Ef = parseFloat(Efen);
		var longitude = Ed + Ef/60 + Em/3600;
       //alert("经度="+longitude);  				
       //经度纬度 度分秒 60进制格式转换成GPS十进制格式结束
			}
               //判断风向开始
                 var fengxiang = ''; 
                 var fxdu = row.probe1;
	        if(fxdu>=0 && fxdu<=22.5) 
		{fengxiang="北风";}
		else if(fxdu>22.5 && fxdu<=67.5)
		{fengxiang="东北风";}
		else if(fxdu>67.5 && fxdu<=112.5)
		{fengxiang="东风";}
		else if(fxdu>112.5 && fxdu<=157.5)
		{fengxiang="东南风";}
		else if(fxdu>157.5 && fxdu<=202.5)
		{fengxiang="南风";}
		else if(fxdu>202.5 && fxdu<=247.5)
		{fengxiang="西南风";}
		else if(fxdu>247.5 && fxdu<=292.5)
		{fengxiang="西风";}
		else if(fxdu>292.5 && fxdu<=337.5)
		{fengxiang="西北风";}
		else 
		{fengxiang="北风";}
              //判断风向结束
	    //赋值到HTML标签ID，这里有ID，HTML页面就要有这个ID标签
		datatime.innerHTML = '' + row.getdatatime + '';
	    temperature1.innerHTML = '' + row.probe7 + '';//两个单引号
		//jiangyuliang.innerHTML = '' + row.probe8.substring(0, 2) + '';
		co1.innerHTML = '' + row.probe8.split("|")[0] + '';
		smog1.innerHTML = '' + row.probe3 + '';
		extinguisher1.innerHTML = '' + row.probe10 + '';
		fireImage1.innerHTML = '' + row.probe10 + '';
		sirenText1.innerHTML = '' + row.probe15 + '';
		sirenImage1.innerHTML = '' + row.probe15 + '';//不确定
		voc1.innerHTML = '' + row.probe2 + '';
		spray1.innerHTML = '' + row.probe11 + '';
		btnControl.innerHTML = '' + row.probe6 + '';
		btnStop.innerHTML = '' + row.probe9 + '';
		btnSpray.innerHTML = '' + row.probe4 + '';
		btnFire.innerHTML = '' + row.probe13 + '';
		wendu.innerHTML = '' + row.probe5 + '';
		fx.innerHTML = '' + row.probe1 + '';
		pm25.innerHTML = '' + row.probe12 + '';
		weidu.innerHTML = '' + latitude + '';       //往html标签写入值，再获得标签内容来传递值
		jingdu.innerHTML = '' + longitude + '';      //没有再通过URL传值，也没有通过全局变量传值
		fengxiangdanwei.innerHTML = fengxiang;//显示风向数值对于的结果 东南西北风
		
		
	    //历史数据框显示的实时数据
	    fengsu0.innerHTML = '' + row.probe7 + '';
		jiangyuliang0.innerHTML = '' + row.probe8 + '';
		qiya0.innerHTML = '' + row.probe3 + '';
		ziwaixian0.innerHTML = '' + row.probe10 + '';
		fushe0.innerHTML = '' + row.probe2 + '';
		co20.innerHTML = '' + row.probe11 + '';
		shidu0.innerHTML = '' + row.probe6 + '';
		guangzhao0.innerHTML = '' + row.probe9 + '';
		diwen0.innerHTML = '' + row.probe4 + '';
		zaoshen0.innerHTML = '' + row.probe13 + '';
		wendu0.innerHTML = '' + row.probe5 + '';
		fx0.innerHTML = '' + row.probe1 + '';
		pm250.innerHTML = '' + row.probe12 + '';
		
		//rHtml.push('<div class="row row-title clearfix">' + row.getdatatime + '</div>');
		//rHtml.push('<a href="/map.html?Ndu=' + Ndu + '&Edu=' + Edu + '" title="GPS地图"><h2 title="' + row.probe15 + '">地图</h2></a>');
	}
	
	return rHtml.join('\n');
}

//历史数据
function readDatalast(isAppend, selector, url, data) {
	
	var lastId = null;
	$.ajax({
		url : url,
		dataType : 'json',
		data: data,
		async : false,
		success: function(data) {
			//console.log(data);
			if (!isAppend) $(selector).html('');
			
			if (data == null) {
				return;
			}
			
			if (!$.isArray(data)) {
				data = [data];
			}
			
			if (isAppend) {
				$(selector).append(getRowHtmllast(data));
			} else {
				$(selector).html(getRowHtmllast(data));
			}
			
			lastId = data[data.length - 1].id;
		}
	});
	
	return lastId;
}

function getRowHtmllast(data) {
	var row;
	var rHtml = [];
	
	
	for (var i = 0; i < data.length; i++) {
		row = data[i];
		
		//数据格式由'' + row.probe7 + ''要换成row.probe7  而且在PHP页面传入的row.probe7数据也要由数据库端的字符型通过intval($rs['probe7'])函数变成整型
	    //由于数组元素数值要参与计算，因此必须是整型，这里就不能加单引号和+号后变成字符型赋给数组
		arrlastData01[i] = row.probe7;
		arrlastData02[i] = parseInt(row.probe8.split("|")[0]);//将String类型转化为int类型
		arrlastData03[i] = row.probe3;
		arrlastData04[i] = row.probe10;
		//gps.innerHTML = '' + row.probe15 + '';
		arrlastData05[i] = row.probe2;
		arrlastData06[i] = row.probe11;
		arrlastData07[i] = row.probe6;
		arrlastData08[i] = row.probe9;
		arrlastData09[i] = row.probe4;
		arrlastData10[i] = row.probe13;
		arrlastData11[i] = row.probe5;
		arrlastData12[i] = row.probe1;
		arrlastData13[i] = row.probe12;
	
		//rHtml.push('<div>' + arrlastData01[i] + '</div>');//调试数据显示观察用
		/* rHtml.push('<div>' + arrlastData02[i] + '</div>');
		rHtml.push('<div>' + arrlastData03[i] + '</div>');
		rHtml.push('<div>' + arrlastData04[i] + '</div>');
		rHtml.push('<div>' + arrlastData05[i] + '</div>');
		rHtml.push('<div>' + arrlastData06[i] + '</div>');
		rHtml.push('<div>' + arrlastData07[i] + '</div>');
		rHtml.push('<div>' + arrlastData08[i] + '</div>');
		rHtml.push('<div>' + arrlastData09[i] + '</div>');
		rHtml.push('<div>' + arrlastData10[i] + '</div>');
		rHtml.push('<div>' + arrlastData11[i] + '</div>');
		rHtml.push('<div>' + arrlastData12[i] + '</div>');
		rHtml.push('<div>' + arrlastData13[i] + '</div>'); */
	}
		fs01.innerHTML = arrlastData01[0];
		fs02.innerHTML = arrlastData01[1];
		fs03.innerHTML = arrlastData01[2];
		fs04.innerHTML = arrlastData01[3];
		fs05.innerHTML = arrlastData01[4];
		fs06.innerHTML = arrlastData01[5];
		fs07.innerHTML = arrlastData01[6];
		
		jyl01.innerHTML = arrlastData02[0];
		jyl02.innerHTML = arrlastData02[1];
		jyl03.innerHTML = arrlastData02[2];
		jyl04.innerHTML = arrlastData02[3];
		jyl05.innerHTML = arrlastData02[4];
		jyl06.innerHTML = arrlastData02[5];
		jyl07.innerHTML = arrlastData02[6];
		
		qy01.innerHTML = arrlastData03[0];
		qy02.innerHTML = arrlastData03[1];
		qy03.innerHTML = arrlastData03[2];
		qy04.innerHTML = arrlastData03[3];
		qy05.innerHTML = arrlastData03[4];
		qy06.innerHTML = arrlastData03[5];
		qy07.innerHTML = arrlastData03[6];
		
		zwx01.innerHTML = arrlastData04[0];
		zwx02.innerHTML = arrlastData04[1];
		zwx03.innerHTML = arrlastData04[2];
		zwx04.innerHTML = arrlastData04[3];
		zwx05.innerHTML = arrlastData04[4];
		zwx06.innerHTML = arrlastData04[5];
		zwx07.innerHTML = arrlastData04[6];
		
		fus01.innerHTML = arrlastData05[0];
		fus02.innerHTML = arrlastData05[1];
		fus03.innerHTML = arrlastData05[2];
		fus04.innerHTML = arrlastData05[3];
		fus05.innerHTML = arrlastData05[4];
		fus06.innerHTML = arrlastData05[5];
		fus07.innerHTML = arrlastData05[6];
		
		co01.innerHTML = arrlastData06[0];
		co02.innerHTML = arrlastData06[1];
		co03.innerHTML = arrlastData06[2];
		co04.innerHTML = arrlastData06[3];
		co05.innerHTML = arrlastData06[4];
		co06.innerHTML = arrlastData06[5];
		co07.innerHTML = arrlastData06[6];
		
		sd01.innerHTML = arrlastData07[0];
		sd02.innerHTML = arrlastData07[1];
		sd03.innerHTML = arrlastData07[2];
		sd04.innerHTML = arrlastData07[3];
		sd05.innerHTML = arrlastData07[4];
		sd06.innerHTML = arrlastData07[5];
		sd07.innerHTML = arrlastData07[6];
		
		gzd01.innerHTML = arrlastData08[0];
		gzd02.innerHTML = arrlastData08[1];
		gzd03.innerHTML = arrlastData08[2];
		gzd04.innerHTML = arrlastData08[3];
		gzd05.innerHTML = arrlastData08[4];
		gzd06.innerHTML = arrlastData08[5];
		gzd07.innerHTML = arrlastData08[6];
		
		diw01.innerHTML = arrlastData09[0];
		diw02.innerHTML = arrlastData09[1];
		diw03.innerHTML = arrlastData09[2];
		diw04.innerHTML = arrlastData09[3];
		diw05.innerHTML = arrlastData09[4];
		diw06.innerHTML = arrlastData09[5];
		diw07.innerHTML = arrlastData09[6];
		
		zs01.innerHTML = arrlastData10[0];
		zs02.innerHTML = arrlastData10[1];
		zs03.innerHTML = arrlastData10[2];
		zs04.innerHTML = arrlastData10[3];
		zs05.innerHTML = arrlastData10[4];
		zs06.innerHTML = arrlastData10[5];
		zs07.innerHTML = arrlastData10[6];
		
	    wd01.innerHTML = arrlastData11[0];
		wd02.innerHTML = arrlastData11[1];
		wd03.innerHTML = arrlastData11[2];
		wd04.innerHTML = arrlastData11[3];
		wd05.innerHTML = arrlastData11[4];
		wd06.innerHTML = arrlastData11[5];
		wd07.innerHTML = arrlastData11[6];
		
		fxiang01.innerHTML = arrlastData12[0];
		fxiang02.innerHTML = arrlastData12[1];
		fxiang03.innerHTML = arrlastData12[2];
		fxiang04.innerHTML = arrlastData12[3];
		fxiang05.innerHTML = arrlastData12[4];
		fxiang06.innerHTML = arrlastData12[5];
		fxiang07.innerHTML = arrlastData12[6];
		
		fc01.innerHTML = arrlastData13[0];
		fc02.innerHTML = arrlastData13[1];
		fc03.innerHTML = arrlastData13[2];
		fc04.innerHTML = arrlastData13[3];
		fc05.innerHTML = arrlastData13[4];
		fc06.innerHTML = arrlastData13[5];
		fc07.innerHTML = arrlastData13[6];
	return rHtml.join('\n');
}
//document.write("<script src='/js/mapapi.js'></script>");//在js中引用另一个js文件