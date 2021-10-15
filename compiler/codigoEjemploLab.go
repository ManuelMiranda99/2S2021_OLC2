// A
t0 = H;

heap[H] = 7;
H = H + 1;

heap[H] = 1;
H = H + 1;
heap[H] = 2;
H = H +1;
heap[H] = 3;
H = H + 1;
heap[H] = 4;	// t7
H = H +1;
heap[H] = 5;
H = H + 1;
heap[H] = 6;
H = H +1;
heap[H] = 7;
H = H + 1;

stack[0] = t0;

// Opcion 1 B
/*
	1 2 3 4 5
	6 7 8 9 0
*/
t1 = H

// GENERAL
heap[H] = 2;
H = H + 1;

// PRIMERA FILA
heap[H] = 5;
H = H + 1;
heap[H] = 1;
H = H + 1;
heap[H] = 2;
H = H +1;
heap[H] = 3;
H = H + 1;
heap[H] = 4;
H = H +1;
heap[H] = 5;
H = H + 1;

// SEGUNDA FILA
heap[H] = 5;
H = H + 1;
heap[H] = 6;
H = H + 1;
heap[H] = 7;
H = H +1;
heap[H] = 8;
H = H + 1;
heap[H] = 9;
H = H +1;
heap[H] = 0;
H = H + 1;

stack[1] = t1;

// Opcion 2 B
	/*
		1 2 3 4 5
		6 7 8 9 0
	*/
	t1 = H;

	t2 = H;
	H = H + 3;

	// LEN
	heap[t2] = 2;
	t2 = t2 + 1;

		t3 = H;

		t4 = H;
		H = H + 6;
		// LEN
		heap[t4] = 5;
		t4 = t4 + 1;

		heap[t4] = 1;
		t4 = t4 + 1;
		heap[t4] = 2;
		t4 = t4 + 1;
		heap[t4] = 3;
		t4 = t4 + 1;
		heap[t4] = 4;
		t4 = t4 + 1;
		heap[t4] = 5;
		t4 = t4 + 1;

	heap[t2] = t3;
	t2 = t2 + 1;

		t5 = H;

		t6 = H;
		H = H + 6;
		// LEN
		heap[t6] = 5;
		t6 = t6 + 1;


		heap[t6] = 6;
		t6 = t6 + 1;
		heap[t6] = 7;
		t6 = t6 + 1;
		heap[t6] = 8;
		t6 = t6 + 1;
		heap[t6] = 9;
		t6 = t6 + 1;
		heap[t6] = 0;
		t6 = t6 + 1;

	heap[t2] = t3;
	t2 = t2 + 1;

	stack[1] = t1;

// Acceso a
t7 = stack[0];

t7 = t7 + 1;
t7 = t7 + 3;
t8 = heap[t7];
print(t8);

// Acceso b[1][1]
t9 = stack[1];

t9 = t9 + 1;	// SKIP DE LEN
t9 = t9 + 0;	// MOVER A POS

t10 = heap[t9];
t10 = t10 + 1;	// SKIP DE LEN
t10 = t10 + 0;	// MOVER A POS

t11 = heap[t10];

print(t11);

// STRUCT
// DECLARACION
t0 = H;
t1 = t0;

H = H + 2;

heap[t1] = 21;
t1 = t1 + 1;

	t2 = H;
	heap[H] = 'M';
	H = H + 1;
	heap[H] = 'a';
	H = H + 1;
	heap[H] = 'n';
	H = H + 1;
	heap[H] = 'u';
	H = H + 1;
	heap[H] = 'e';
	H = H + 1;
	heap[H] = 'l';
	H = H + 1;
	heap[H] = -1;
	H = H + 1;

heap[t1] = t2;
t1 = t1 + 1;

stack[0] = t0;

// Acceso a edad.numero
t3 = stack[0];
t3 = t3 + 0;

t4 = heap[t3];
print(t4);

// Asignar a c.nombre.primero
t5 = H;

heap[H] = 'P';
H = H + 1;
heap[H] = 'a';
H = H + 1;
heap[H] = 'b';
H = H + 1;
heap[H] = 'l';
H = H + 1;
heap[H] = 'o';
H = H + 1;
heap[H] = -1;
H = H + 1;

t6 = stack[0];
t6 = t6 + 1;

heap[t6] = t5;