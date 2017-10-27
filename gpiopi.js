var fs=require('fs');
var path='/sys/class/gpio/';
module.exports={
	low:function(pin){
        fs.exists(path+'gpio'+pin+'/value',function (exists) {
            if(exists){
                fs.writeFile(path+'unexport',pin,function(){
                    fs.writeFile(path+'export',pin,function(){
                        fs.writeFile(path+'gpio'+pin+'/direction','out',function(){
                            fs.writeFile(path+'gpio'+pin+'/value',0);
                        });
                    });
                });
            }else{
                fs.writeFile(path+'export',pin,function(){
                    fs.writeFile(path+'gpio'+pin+'/direction','out',function(){
                        fs.writeFile(path+'gpio'+pin+'/value',0);
                    });
                });
            }
        });
    },
    high:function(pin){
        fs.exists(path+'gpio'+pin+'/value',function (exists) {
            if(exists){
                fs.writeFile(path+'unexport',pin,function(){
                    fs.writeFile(path+'export',pin,function(){
                        fs.writeFile(path+'gpio'+pin+'/direction','out',function(){
                            fs.writeFile(path+'gpio'+pin+'/value',1);
                        });
                    });
                });
            }else{
                fs.writeFile(path+'export',pin,function(){
                    fs.writeFile(path+'gpio'+pin+'/direction','out',function(){
                        fs.writeFile(path+'gpio'+pin+'/value',1);
                    });
                });
            }
        });
	}
}
