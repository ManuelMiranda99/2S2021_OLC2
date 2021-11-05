print(5 + 5);
println(1 * 100 / 2);
println(5 > 0);
println(true);
println((5 == 10) == false);
println((5 == 10) && (1 != 1));
println((5 == 10) || (1 == 1));

a = (10 + 10) * (8 / (2+2));
b = "Que tal";
c = true;

println("Hola Mundo!");
println(a);
println(b);
println(c);

if true
    println(true)
end;

if 5 > 1
    println("If Normal");
end;

# IF ELSE
if (5 - 10) < 0
    println("If Else");
else
    println("If Else en else");
end;

# IF ELSEIF
if 1 >= 2
    println("If Elseif");
elseif 1 <= 1
    println("If Elseif en elseif");
end;

# IF ELSEIF ELSE
if 10 == 11
    println("If Elseif Else");
elseif 10 != 11
    println("If Elseif Else en Elseif");
else
    println("If Elseif Else en Else");
end;


# IF ELSEIF*2 ELSE
if false
    println("If Elseif*2 Else");
elseif true
    println("If Elseif*2 Else en Elseif1");
elseif false
    println("If Elseif*2 Else en Elseif2");
else
    println("If Elseif*2 Else en Else");
end;

if 5 > 1
    println("If Normal");
    if true
        println("If dentro de If");
        if false
            println("If dentro de If dentro de If");
        else
            println("If dentro de If dentro de If en Else");
        end;
    elseif false
        println("Else if dentro de If");
    else
        println("Else dentro de If");
    end;
end;

a = 10;
while a > 0
    print("El valor de a es: ");
    println(a);
    a = a - 1;
end;

while a < 5
    a = a + 1;
    if a == 3
        println("a");
        continue;
    elseif a == 4
        println("b");
        break;
    end;
    print("El valor de a es: ");
    println(a);
end;

function suma(a::Int64, b::Int64)::Int64
    return a + b;
end;

println(suma(10, 20));

#=
/*----HEADER----*/
package main;

import (
	"fmt"
);

var t0, t1, t2, t3, t4 float64;
var P, H float64;
var stack [30101999]float64;
var heap [30101999]float64;

func main(){

	t0=5-10;                        // Lider
	if t0 < 0 {goto L0;}
	goto L1;                        // Lider
	
	L0:                             // Lider
	fmt.Printf("%d", int(1));
	fmt.Printf("%c", int(10));
	goto L2;
	L1:                             // Lider
	fmt.Printf("%d", int(0));
	fmt.Printf("%c", int(10));
	L2:                             // Lider
	stack[int(0)]=10;
	
	L3:                             // Lider
	t1=stack[int(0)];
	
	if t1 > 0 {goto L4;}
	goto L5;                        // Lider
	
	L4:                             // Lider
	t2=stack[int(0)];
	
	fmt.Printf("%d", int(t2));
	fmt.Printf("%c", int(10));
	t3=stack[int(0)];
	
	t4=t3-1;
	stack[int(0)]=t4;
	
	goto L3;
	L5:                             // Lider
}
=#