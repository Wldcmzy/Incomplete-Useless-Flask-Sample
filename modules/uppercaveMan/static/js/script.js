$(document).ready(function() {
    $('.artist_l li').each(function(m) {
		//榧犳爣杩樻病缁忚繃锛屾牱寮忓垵濮嬪寲鐨勮缃紝鎺у埗娴姩鍖哄煙搴曠殑浣嶇疆锛屽垵濮嬬姸鎬佷篃瑕侀伩鍏嶉噸鍙�
        $(this).find('a').css('top', -$(this).height()-50);
		
		//榧犳爣缁忚繃鎮仠涓婃柟鐨勮繃绋�
        $(this).hover(function() {
            $(this).find('a').animate({
				//椤堕儴閲嶅悎
                'top': '0'	
            },
			//鍔ㄧ敾鏃堕棿 鍗曚綅璞
            200)
        },//鏂囧瓧浠庨《寰€涓嬫粦鍑轰笌搴曟牸瀛愰噸鍚�
		
		//鏂囧瓧鍚戜笅婊戝嚭娑堝け鐨勮繃绋�
        function() {
            $(this).find('a').animate({
				//
                'top': $(this).height()+45
            },
            {
				//鍔ㄧ敾鏃堕棿 鍗曚綅璞
                duration: 300,
                complete: function() {
					//榧犳爣缁忚繃鍚庯紝娴姩鍖哄煙涓庡搴斿尯鍧楃殑涓婁笅闂磋窛锛岄伩鍏嶉噸鍙�
                    $(this).css('top', -$(this).parent('li').height()-50)
                }
            })
        })
    });
});