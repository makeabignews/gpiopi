var fs=require('fs');
var path='/sys/class/gpio/';
module.exports={
	in:function(number){
        if(!fs.existsSync(path+'gpio'+number+'/value')){
            fs.writeFileSync(path+'export',number);
			fs.writeFileSync(path+'gpio'+number+'/direction','in');
        }
	    var contentText = fs.readFileSync(path+'gpio'+number+'/value','utf-8');
		var value=parseInt(data);
		return value;
	},
	out:function(number,value){
        if(!fs.existsSync(path+'gpio'+number+'/value')){
            fs.writeFileSync(path+'export',number);
			fs.writeFileSync(path+'gpio'+number+'/direction','out');
        }
		fs.writeFileSync(path+'gpio'+number+'/value',value);
	},
	clear:function(number){
		fs.writeFileSync(path+'unexport',number);
	}
}
