window.onload=BDmap; //鏈€鍚庡姞杞芥js鏂囦欢
function BDmap(){ 
	// 鐧惧害鍦板浘API鍔熻兘
	var map = new BMap.Map("allmap");
	map.centerAndZoom(new BMap.Point(121.235618,31.129118),11);
	map.enableScrollWheelZoom(true);
        var myDis = new BMapLib.DistanceTool(map);
//娴嬭窛寮€濮�
var contextMenu = new BMap.ContextMenu();//鍒涘缓鍙抽敭瀵硅薄
var txtMenuItem = [
  { text:'娴嬭窛',callback:function(){myDis.open()}},
  { text:'鍦ㄦ娣诲姞鏍囨敞',
   callback:function(p){
    var marker = new BMap.Marker(p), px = map.pointToPixel(p);
    map.addOverlay(marker);
   }
  }
 ];
for(var i=0; i < txtMenuItem.length; i++){
 contextMenu.addItem(new BMap.MenuItem(txtMenuItem[i].text,txtMenuItem[i].callback,100));
 if(i==1 || i==3) {
  contextMenu.addSeparator();
 }
}
map.addContextMenu(contextMenu);
//===================娴嬭窛缁撴潫
 //鑾峰彇鍦板潃鏍忓瓧绗︿覆          
 /*     function getUrlVars(){
        var vars = [], hash;
        var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
        for (var i = 0; i < hashes.length; i++) {
            hash = hashes[i].split('=');
            vars.push(hash[0]);
            vars[hash[0]] = hash[1];
        }
        return vars;
    }  
        var Ndu=getUrlVars()["Ndu"];
        var Edu=getUrlVars()["Edu"]; 
 */
 //鑾峰彇鍦板潃鏍忓瓧绗︿覆
 
       	var Edu = parseFloat(document.getElementById("jingdu").innerText);  //鍔犱笂鍋忕Щ閲�0.003250
          //var Edu = 121.4029295904;
		  //alert("jingdu1="+Edu);  //璋冭瘯鐢�
        var Ndu = parseFloat(document.getElementById("weidu").innerText);  //鍔犱笂鍋忕Щ閲�0.002100
            //var Ndu = 31.2189051366;
			//alert("weidu1="+Ndu);  
			console.error( '缁忕含搴︿负'+Edu+'|'+Ndu );
	// 鐢ㄧ粡绾害璁剧疆鍦板浘涓績鐐�
		if(Edu != "" && Ndu != ""){
			map.clearOverlays(); 
			var new_point = new BMap.Point(Edu,Ndu);//鏈浆鎹㈢殑GPS鍧愭爣 鏄剧ず鍦ㄧ櫨搴﹀湴鍥句笂鍋忓樊寰堝ぇ
			var marker = new BMap.Marker(new_point);  // 鍒涘缓鏍囨敞
			//map.addOverlay(marker);              // 灏嗘爣娉ㄦ坊鍔犲埌鍦板浘涓� 涓嶆樉绀烘湭杞崲鐨刉GS84鍧愭爣
			map.panTo(new_point);  
//var opts = {width : 100,height: 50,title : "鎴戠殑浣嶇疆"}
//var infoWindow = new BMap.InfoWindow(" ", opts);  // 鍒涘缓淇℃伅绐楀彛瀵硅薄
//map.openInfoWindow(infoWindow,new_point);
//marker.addEventListener("click", function(){map.openInfoWindow(infoWindow,new_point);});

//var sContent ="鎴戠殑浣嶇疆";
//var infoWindow = new BMap.InfoWindow(sContent);  // 鍒涘缓淇℃伅绐楀彛瀵硅薄
//map.openInfoWindow(infoWindow,new_point); //寮€鍚俊鎭獥鍙�
//marker.addEventListener("click", function(){map.openInfoWindow(infoWindow,new_point);});
		}
        var top_left_control = new BMap.ScaleControl({anchor: BMAP_ANCHOR_TOP_LEFT});  
        var top_left_navigation = new BMap.NavigationControl({anchor: BMAP_ANCHOR_TOP_LEFT}); 
        map.addControl(top_left_control);
        map.addControl(top_left_navigation);

        var mapType1 = new BMap.MapTypeControl({mapTypes: [BMAP_NORMAL_MAP,BMAP_HYBRID_MAP]});
        //var overView = new BMap.OverviewMapControl();
        //var overViewOpen = new BMap.OverviewMapControl({isOpen:true, anchor: BMAP_ANCHOR_BOTTOM_RIGHT});
        map.addControl(mapType1);//娣诲姞鍗槦鍥炬贩鍚堝浘
        //map.addControl(overView);
        //map.addControl(overViewOpen);//娣诲姞缂╃暐鍥�

        map.setMapStyle({style:'midnight'});//鍗堝钃濇牱寮�
		
//鍧愭爣杞崲瀹屼箣鍚庣殑鍥炶皟鍑芥暟
    translateCallback = function (data){
      if(data.status === 0) {
        var markerbd = new BMap.Marker(data.points[0]);
        map.addOverlay(markerbd);
        var label = new BMap.Label("鎴戠殑姘旇薄绔�",{offset:new BMap.Size(20,-10)});
        markerbd.setLabel(label); //娣诲姞label
        map.setCenter(data.points[0]);
      }
    }

    setTimeout(function(){
        var convertor = new BMap.Convertor();
        var pointArr = [];
        pointArr.push(new_point);
        convertor.translate(pointArr, 1, 5, translateCallback)//鏈浆鎹㈢殑GPS鍧愭爣銆佸師濮嬪潗鏍囥€佺‖浠躲€佽胺姝屽湴鐞冨潗鏍囪浆鐧惧害鍧愭爣  1,5
    }, 1000);
	
//杞崲瀹屾垚
	
//娣诲姞鐐瑰嚮鍦板浘鐩戝惉浜嬩欢锛岀偣鍑诲湴鍥惧悗鏄剧ず褰撳墠缁忕含搴�
//	function showInfo(e){
//		alert(e.point.lng + ", " + e.point.lat);
//	}
//	map.addEventListener("click", showInfo);	
};