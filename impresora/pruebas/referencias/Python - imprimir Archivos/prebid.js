pbjs.sas_65d66bfd601f7ae({"cpm":0.1,"currency":"EUR","width":728,"height":90,"ad":"<html><body><script type='text/javascript'>var sas = sas || {};\r\nsas.utils = sas.utils || {};\r\nif (!sas.utils.cdns) {\r\n  sas.utils.cdns = {\r\n    \"http:\" : \"http://ced-ns.sascdn.com\",\r\n    //\"http:\" : \"http://demo.smartadserver.com\",\r\n    \"https:\" : \"https://ced-ns.sascdn.com\"\r\n  }\r\n}\r\n\r\nvar sas=sas||{};sas.utils=sas.utils||{};sas.events=sas.events||{};sas.rev=sas.rev||20110214;(function(){if(!sas.utils.cdns){sas.utils.cdns={\"http:\":\"http://ak-ns.sascdn.com\",\"https:\":\"https://ec-ns.sascdn.com\"}}else{if(!sas.utils.cdns[\"http:\"]||sas.utils.cdns[\"http:\"].length==0){sas.utils.cdns[\"http:\"]=\"http://ak-ns.sascdn.com\"}if(!sas.utils.cdns[\"https:\"]||sas.utils.cdns[\"https:\"].length==0){sas.utils.cdns[\"https:\"]=\"https://ec-ns.sascdn.com\"}}var e=function(){};sas.utils.getIEVersion=function(){var g=navigator.userAgent.match(/(?:MSIE |Trident\\/.*; rv:)(\\d+)/);return g?parseInt(g[1]):undefined};sas.events.addEvent=function(h,g,i){if(!h||!g||!i){return}if(h.attachEvent){h.attachEvent(\"on\"+g,i)}else{if(h.addEventListener){h.addEventListener(g,i,false)}}return{removeEvent:function(){if(h.detachEvent){h.detachEvent(\"on\"+g,i)}else{if(h.removeEventListener){h.removeEventListener(g,i,false)}}}}};sas.events.addLoadEvent=function(h,l){if(!h||!l){return}var g=\"load\";var i=function(){return true};var k=sas.utils.getIEVersion();if(k<11||h==document){g=\"readystatechange\";i=function(){if(!h.readyState||h.readyState==\"complete\"||h.readyState==\"loaded\"||h.readyState==4){return true}}}var j=sas.events.addEvent(h,g,function(){if(i()){j.removeEvent();l.apply(this,arguments)}})};sas.utils.Latch=function(n){n=n||[];var m=[];var l={};var k=n;var h=false;for(var j=0;j<k.length;j++){l[n[j]]={}}var o=function(){if(h){return}for(var p in l){if(!l[p].status){return}}h=true;var r=g();for(var q=0;q<m.length;q++){m[q].apply(this,r)}};var g=function(){var q=[];for(var p=0;p<k.length;p++){q.push(l[k[p]].result)}return q};this.notify=function(p,i){if(!l[p]){return}else{l[p].status=true;l[p].result=i;o()}};this.addListener=function(i){if(i!=null){h?i():m.push(i)}};o()};sas.utils._libs=sas.utils._libs||{};var b=function(h,g){if(h.charAt(h.length-1)==\"/\"){h=h.slice(0,-1)}if(g.charAt(0)==\"/\"){g=g.slice(1)}return h+\"/\"+g};var c=function(h){if(typeof h===\"string\"){h=[h]}var k=(document.location.protocol==\"https:\");var g=k?sas.utils.cdns[\"https:\"]:(sas.utils.cdns[document.location.protocol]||sas.utils.cdns[\"http:\"]);for(var j=0;j<h.length;j++){h[j]=b(g,h[j])}return h};sas.utils.loadLinkCdn=function(g){g=c(g);for(var h=0;h<g.length;h++){a(g[h],true)}};sas.utils.loadScriptCdn=function(g,h){g=c(g);sas.utils.loadScript(g,h)};var f=Math.floor(Math.random()*1000000);var d=1;sas.utils._callbacks=sas.utils._callbacks||{};var a=function(k,h,g,j){var l=(h?\"link\":\"script\")+\"-\"+f+\"-\"+d++;var i=document.createElement(h?\"link\":\"script\");i.id=l;i.setAttribute(\"type\",h?\"text/css\":\"text/javascript\");i.setAttribute(h?\"href\":\"src\",k);if(h){i.setAttribute(\"rel\",\"stylesheet\")}if(!h&&g){i.setAttribute(\"async\",\"true\")}sas.utils._libs[k]={loaded:false,callbacks:[]};if(j!=null){sas.utils._libs[k].callbacks.push(j)}sas.utils._callbacks[l]=(function(m){return function(){sas.utils._libs[m].loaded=true;for(var n=0;n<sas.utils._libs[m].callbacks.length;n++){sas.utils._libs[m].callbacks[n]()}}})(k);if(h||g){document.getElementsByTagName(\"head\")[0].appendChild(i);sas.events.addLoadEvent(document.getElementById(l),sas.utils._callbacks[l])}else{document.write(i.outerHTML);document.write(\"<script type='text/javascript'>(function() { sas.utils._callbacks['\"+l+\"'](); })();<\\/script>\")}};sas.utils.loadScript=function(h,j){j=j||{};j.async=j.async==null?true:j.async;var l=j.onLoad||e;if(typeof h===\"string\"){h=[h]}var m=new sas.utils.Latch(h);m.addListener(l);for(var k=0;k<h.length;k++){var n=h[k];var g=(function(i){return function(){m.notify(i)}})(n);if(!sas.utils._libs[n]){a(n,false,j.async,g)}else{if(sas.utils._libs[n].loaded){m.notify(n)}else{sas.utils._libs[n].callbacks.push(g)}}}}})();\r\n\r\n(function() {\r\n\r\nvar tag = document.getElementById('wfg_ad-LDB2');\r\nif (!tag) {\r\n  document.write(\"<div id='wfg_ad-LDB2'></div>\");\r\n} else {\r\n  /* Pre-create something in the DOM to have the sas_loadHandler to work */\r\n  var d = document.createElement(\"div\");\r\n  d.style.display = \"none\";\r\n  tag.appendChild(d);\r\n}\r\n\r\nvar sas = window.sas;\r\n// used to detect ajax call for pubj\r\nvar isAsync = window.sas_ajax || true;\r\n\r\n// Config \r\nvar config = {\r\n        id: 6787554,\r\n        formatId: 55858,\r\n        tagId: \"wfg_ad-LDB2\",\r\n        instanceIndex: 1,\r\n        customScript: '',\r\n        forcedIframeWidth: 0,\r\n        forcedIframeHeight: 0,\r\n        oba: 0,\r\n        creatives:\r\n        [{\r\n          id: '0',\r\n          type: 0,\r\n          url: '',\r\n          countUrl: '',\r\n          clickUrl: 'http://prg.smartadserver.com/click?imgid=0&insid=6787554&pgid=776430&uid=6029627832547788319&tgt=%24dt%3d1t%3bpos%3dldb2%3b%24hc&systgt=%24qc%3d1312393061%3b%24ql%3dmedium%3b%24qpc%3d01000%3b%24qpp%3d0%3b%24qt%3d47_1472_3249t%3b%24dma%3d0%3b%24b%3d12540%3b%24o%3d99999&rtb=1&rtbnid=2496&rtbbid=377837793850426626&rtbh=b0a3016df85c314d9f7e4f6873512728c18933f8&rtblt=636366817728000247&rtbet=0&pgDomain=http%3a%2f%2fwww.lawebdelprogramador.com%2fforos%2fPython%2f1355152-imprimir.html&go=',\r\n          clickTarget: '_blank',\r\n          clickUrlArray: [\"http://prg.smartadserver.com/click?imgid=0&insid=6787554&pgid=776430&uid=6029627832547788319&tgt=%24dt%3d1t%3bpos%3dldb2%3b%24hc&systgt=%24qc%3d1312393061%3b%24ql%3dmedium%3b%24qpc%3d01000%3b%24qpp%3d0%3b%24qt%3d47_1472_3249t%3b%24dma%3d0%3b%24b%3d12540%3b%24o%3d99999&rtb=1&rtbnid=2496&rtbbid=377837793850426626&rtbh=b0a3016df85c314d9f7e4f6873512728c18933f8&rtblt=636366817728000247&rtbet=0&pgDomain=http%3a%2f%2fwww.lawebdelprogramador.com%2fforos%2fPython%2f1355152-imprimir.html&go=\"],\r\n          width: '728',\r\n          height: '90',\r\n          pixelRatio: '1',\r\n          altText: '',\r\n          creativeScript: '<img src=\\'http://prg.smartadserver.com:80/h/aip?visit=S&amp;pubid=31&amp;statid=1&amp;ckid=6029627832547788319&amp;tmstp=333512616&amp;usrtgt=&amp;tgt=%24dt%3d1t%3bpos%3dldb2%3b%24hc&amp;systgt=%24qc%3d1312393061%3b%24ql%3dmedium%3b%24qpc%3d01000%3b%24qpp%3d0%3b%24qt%3d47_1472_3249t%3b%24dma%3d0%3b%24b%3d12540%3b%24o%3d99999&amp;pgDomain=http%3a%2f%2fwww.lawebdelprogramador.com%2fforos%2fPython%2f1355152-imprimir.html&amp;capp=0&amp;mcrdbt=0&amp;insid=6787554&amp;imgid=0&amp;pgid=776430&amp;fmtid=55858&amp;loguid=377837793850426610&amp;logdate=1501084972800&amp;sig=kR%2f4WOPdyRcXZxemURbeeladWw7mNG7joDWKDb4vNGk%3d&amp;rtb=1&amp;rtbnid=2496&amp;rtbbid=377837793850426626&amp;rtbh=b0a3016df85c314d9f7e4f6873512728c18933f8&amp;rtblt=636366817728000247&amp;rtbet=0\\' border=\\'0\\' width=\\'0\\' height=\\'0\\' style=\\'display:none\\'/><iframe src=\\'https://ec-ns.sascdn.com:443/diff/rtb/handler/st.min.html?%7b%22bid%22%3a%22377837793850426626%22%2c%22adomain%22%3a%22att.com.mx%22%2c%22page%22%3a%22776430%22%2c%22format%22%3a%2255858%22%2c%22crid%22%3a%2218833403%22%2c%22dsp%22%3a%2222%22%2c%22buyer%22%3a%229792%22%2c%22cid%22%3a%22726471%22%2c%22adid%22%3a%2218833403%22%2c%22hash%22%3a%22-6460763550941154475%22%7d\\' width=\\'0\\' scrolling=\\'no\\' height=\\'0\\' frameborder=\\'0\\' style=\\'display: none;\\'></iframe><scr'+'ipt type=\\'text/javascript\\' src=\\'http://a2.adform.net/adfscript/?bn=18833403;rtbwp=r-H9i-cobpTVijFTJmcyTUhbTecyPNQM0M2T5Q;rtbdata=A9AFjFBzKpRWa4sVrhnZGT2tUdzEx61NEXX4_nOpKi-yetSZc70uSNQjqnm9NlQvenobZ55XuluqvN6KOOUwrzXNWwuJIsxR21XqbSGCVM3OgxjpC2bou2X2jGdjR4V9z6p3ABy7cXQzlENmcQVVSVvaPdJvZVD0jF2DhtVmGrCHuXYjV6PPhd-UacF6RJEF36nIGy430M8Nk1fH4YMihrpoC6VE74xooiKO4TsXZEoJUs5FSsegbXzG0KEkH6Aw6kwTf3MRIqr7QDJom3ErsbrPJs9pB-zRtrt4CK66h2W0UiK4a-CD6CCZhYPGDUi40\\'></scr'+'ipt>',\r\n          flashVars: '',\r\n          version: '',\r\n          wMode: 'Opaque',\r\n          backupImage: {\r\n            id: '',\r\n            type: 1,\r\n            url: '',\r\n            clickUrl: '',\r\n            clickTarget: '',\r\n            width: '',\r\n            height: '',\r\n            altText: ''\r\n          }\r\n        }]\r\n      };\r\n\r\nif(sas.utils.getIEVersion() < 10 && !isAsync){\r\n// IE9- require full script injection in sync case.\r\n  \r\n  \r\n  \r\n  sas.banner.render(config, {async: isAsync});\r\n}else{\r\n  sas.utils.loadScriptCdn(\"/diff/templates/js/sas/sas-browser.js\", { async: isAsync, onLoad: function() {\r\n    sas.utils.loadScriptCdn(\"/diff/templates/js/sas/sas-dom.js\", { async: isAsync, onLoad: function() {\r\n    sas.utils.loadScriptCdn(\"/diff/templates/js/banner/sas-banner-2.4.js\", { async: isAsync, onLoad: function() {\r\n      sas.banner.render(config, {async: isAsync});\r\n    }});\r\n  }});\r\n}});\r\n}\r\n})();</script></body></html>","dealId":null});