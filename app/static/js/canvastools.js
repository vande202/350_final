
function handlecanvasClick(AOM,xin,yin) {


    function getClickedObject(AOM, xin, yin) {
        var rect = canvas.getBoundingClientRect();
        x = xin - rect.left
        y = yin - rect.top
        var minx = 0
        var miny = 0
        var maxx = 0
        var maxy = 0
        var stateflag=getStateflag(AOM);


        for (var i = 0, size = AOM.length; i < (size); i++) {
            if (AOM[i].flag==stateflag) {
                if (AOM[i].type == 'reddot') {


                    minx = AOM[i].x_cord;
                    miny = AOM[i].y_cord;
                    maxx = AOM[i].x_cord + AOM[i].width;
                    maxy = AOM[i].y_cord + AOM[i].height;
                    if (x > minx && x < maxx) {
                        if (y > miny && y < maxy) {
                            return (AOM[i]);
                        }
                    }
                }
                if (AOM[i].type == 'floorportal') {
                                        minx = AOM[i].x_cord;
                    miny = AOM[i].y_cord;
                    maxx = AOM[i].x_cord + AOM[i].width;
                    maxy = AOM[i].y_cord + AOM[i].height;
                    if (x > minx && x < maxx) {
                        if (y > miny && y < maxy) {
                            return (AOM[i]);
                        }
                    }


                }
            }
        }
    }


    var clicked_object=getClickedObject(AOM,xin,yin);
        if (clicked_object.type=='reddot'|| clicked_object.type=='floorportal'){
            var newflag=clicked_object.pointer;;

            AOM=setStateFlag(AOM,newflag);
            activatEachAOM(AOM);


        }
}


function preloadimages(arr){
    var newimages=[];
    var postaction=function(){};
    var newimages=[], loadedimages=0;

    var arr=(typeof arr!="object")? [arr] : arr //force arr parameter to always be an array

    function imageloadpost(){
        loadedimages++;
        if (loadedimages==arr.length){
            //alert("All images have loaded (or died trying)!")
            postaction(newimages)
        }
    }


    for (var i=0; i<arr.length; i++){
        newimages[i]=new Image();
        newimages[i].src=arr[i];

        newimages[i].onload=function(){
            imageloadpost()
        };
        newimages[i].onerror=function(){
            alert("imagelloaderror >:<");
        imageloadpost()
        }
    }
    return { //retun blank object  with done() method
        done:function(f){
            postaction=f|| postaction
        }



    }




}

function getStateflag(AOM){
    for (var i=0,size=AOM.length;i<(size);i++) {

        if (AOM[i].type == 'config') {
            return(AOM[i].stateflag);

        }
    }

}

function getMaxStack(AOM){
    for (var i=0,size=AOM.length;i<(size);i++) {

        if (AOM[i].type == 'config') {
            return(AOM[i].maxstack);

        }
    }

}

function setStateFlag(AOM,newflag){
    for (var i=0,size=AOM.length;i<(size);i++) {
        if (AOM[i].type == 'config') {

            AOM[i].stateflag=newflag.valueOf();

            return(AOM);

        }
}


}



function activatEachAOM(AOM){
    //determine shown state flag, ei what subset of objects will be shown
    var stateflag=getStateflag(AOM);
    var maxstack=getMaxStack(AOM)
    //build canvas and context
    var c = document.getElementById("canvas");
    var ctx = c.getContext("2d");
    ctx.imageSmoothingEnabled=false;
    ctx.clearRect(0,0,c.width,c.height);

    //build image array for preloading
    var arr=[];
    for (var i=0,size=AOM.length;i<(size);i++) {

        if (AOM[i].type == 'image') {
            if (AOM[i].flag==stateflag) {
                arr.push(AOM[i].src)
            }



        }

    }

    //once image preloading has been done,
    preloadimages(arr).done(function(images){
        var j=0;

        var stack=1;
        while(stack!=maxstack) {
            for (var i = 0, size = AOM.length; i < (size); i++) {
                if (AOM[i].flag == stateflag) {
                    if (AOM[i].stack == stack) {

                        ///image case
                        if (AOM[i].type == 'image') {
                            var ctx = canvas.getContext("2d");
                            ctx.drawImage(images[j], AOM[i].x_cord, AOM[i].y_cord, AOM[i].width, AOM[i].height);
                            j++;
                        }

                        //redot portal case
                        if (AOM[i].type == 'reddot') {
                            //alert("reddot")
                            var ctx = canvas.getContext("2d");
                            ctx.fillStyle = "#FF0000";
                            ctx.fillRect(AOM[i].x_cord, AOM[i].y_cord, AOM[i].width, AOM[i].height);

                        }
                        //floorportalcase
                        if (AOM[i].type == 'floorportal') {
                            var ctx = canvas.getContext("2d");
                            ctx.fillStyle = "#FF0000";
                            ctx.font = "30px Arial";
                            var textstring=AOM[i].pointer;
                            ctx.fillRect(AOM[i].x_cord, AOM[i].y_cord, AOM[i].width, AOM[i].height);
                            ctx.fillText(textstring,AOM[i].x_cord, AOM[i].y_cord);


                        }
                        // line case
                        if (AOM[i].type == 'line') {
                            var ctx = canvas.getContext("2d");
                            ctx.beginPath();
                            ctx.moveTo(AOM[i].x_origin, AOM[i].y_origin);
                            ctx.lineTo(AOM[i].x_destination, AOM[i].y_destination);
                            ctx.stroke();


                        }

                    }
                }


            }

            stack++

        }





    })





}