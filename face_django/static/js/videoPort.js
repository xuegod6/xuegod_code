$(document).ready(function(){
    // 这里设置一个全局变量， 作为图像base64
    var imgdata = null;
    $('.loadbtn').click(function(){
        jQuery('.video_port').show();
        function $(elem) {
            return document.querySelector(elem);
        };

        var canvas = document.getElementById("vi_canver");
        var context = canvas.getContext("2d");
        var video = $('#video'),
            screen = $('#screenshots'),
            close = $('#close'),
            mediaStream;

        //打开摄像头主要用到下面的getUserMedia方法，用来将获取到的媒体流传入video标签中
        navigator.mediaDevices.getUserMedia({
            video: true
        }).then(function(stream) {
            // 这里面写成功的回调函数
            console.log(stream);
            mediaStream = typeof stream.stop === 'function' ? stream : stream.getTracks()[1];
            video.src = (window.URL || window.webkitURL).createObjectURL(stream);
            video.play();
        }).catch(function(error) {
            // 这里是失败的回调
            console.log(error);
        })
        // 这里截取图片的原理为截取video画面中的当前帧，然后使用canvas中drawImage方法将内容绘至canvas中
        screen.addEventListener('click', function() {
            context.drawImage(video, 0, 0, 400, 300);
            var type = 'jpeg';
            //在这里我直接将canvas中的内容转化为base64格式，传入到需要显示的img中
            imgdata = canvas.toDataURL(type)
            jQuery("#uploadimg").attr("src",imgdata);
        }, false);
        // 关闭摄像头
        close.addEventListener('click', function() {
            mediaStream && mediaStream.stop();
            jQuery('.video_port').hide();
        }, false);
    });

    // 这是一个转换base64的一个方法
    function convertBase64UrlToBlob(urlData){

        var bytes=window.atob(urlData.split(',')[1]);        //去掉url的头，并转换为byte

        //处理异常,将ascii码小于0的转换为大于0
        var ab = new ArrayBuffer(bytes.length);
        var ia = new Uint8Array(ab);
        for (var i = 0; i < bytes.length; i++) {
            ia[i] = bytes.charCodeAt(i);
        }

        return new Blob( [ab] , {type : 'image/jpeg'});
    }

    $('.uploadbtn').click(function(){
        //这里用formDate对象向后端传输文件完成交互
        var formDate = new FormData();
        formDate.append('image', convertBase64UrlToBlob(imgdata));
        var csrftoken = $('input[name ="csrfmiddlewaretoken"]').val();
        $.ajax({
            type: 'POST',
            url: '/index/',
            data: formDate,
            contentType: false,
            processData: false,
            dataType:'text',
            success: function(data){
                alert(data);
            },
            error: function(data){
                alert('error');
            },
            beforeSend:function (xhr,settings) {
                xhr.setRequestHeader("X-CSRFToken",csrftoken)
            },

        })
    })

});
