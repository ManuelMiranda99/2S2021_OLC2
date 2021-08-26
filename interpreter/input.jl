a = 0;
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

