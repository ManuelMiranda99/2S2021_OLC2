proc uno(int x, REF int y){
    y = y + x;
}

proc dos(){
    int x, y;
    x = 1;
    y = 2;
    uno(y,x);
}

dos();

/*   C3D    */
func uno(){
    t1 = P + 1;
    t2 = stack[t1];     // Obtención de referencia parámetro y

    t3 = P + 1;
    t4 = stack[t3];
    t5 = stack[t4];     // Obtención del valor del parámetro por referencia y

    t6 = P + 0;
    t7 = stacfk[t6];    // Obtención de parámetro x
    
    t8 = t5 + t7;       // y = y + x;

    stack[t2] = t8;
}

func dos(){
    t9 = P + 0;
    stack[t9] = 1;

    t10 = P + 1;
    stack[t10] = 2;

    // Parametros
    /* Parametro 1 */
    // Paso 1
        t11 = P + 1;
        t12 = stack[t11];
    // Paso 2.1
        t13 = P + 2;    // Cambio simulado de ambito
    // Paso 2.2
        t14 = t13 + 0;  // Posicion en el nuevo ambito
    // Paso 3
        stack[t14] = t12;   // Guardar en el nuevo ambito
    /* Parametro 2 */
    // Paso 1
        t15 = P + 0;    // Como es parametro por referencia, se pasa la posicion en memoria donde se encuentra actualmente
    // Paso 2.1
        t16 = P + 2;    // Cambio simulado de ambito
    // Paso 2.2
        t17 = t16 + 1;  // Posicion en el nuevo ambito
    // Paso 3
        stack[t17] = t15;
    
    // Paso 4
        P = P + 2;  // Cambio de ambito
    // Paso 5
        uno();
    // Paso 5
        P = P - 2;  // Regreso de ambito
}

func main(){
    P = P + 0;
    dos();
    P = P - 0;
}