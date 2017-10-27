# gpiopi
use:

```bash
npm install gpiopi
```

read a pin value

```nodejs
var gpiopi=require('gpiopi');
var pinvalue=gpiopi.in(2);
```

set a pin LOW or HiGH

```nodejs
gpiopi.out(21,1);//high
gpiopi.out(21,0);//low
```

新浪微博 @谷三井
