
println(true);
println(false);
println("Hola");
print(2 + 2);
println(2.5 - 2);

# IF NORMAL
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

# Ifs anidados
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
    if a == 3
        println("a");
        # continue;
    elseif a == 4
        println("b");
        # break;
    end;
    
    print("El valor de a es: ");
    println(a);
    a = a + 1;
end;

function suma(a, b)
    return a + b;
end;

println(suma(10, 5));