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