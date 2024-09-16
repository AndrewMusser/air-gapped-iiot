PROGRAM _INIT
	
	id := 'MACHINE_35C';
	packMLState := 'EXECUTE';
	

END_PROGRAM

PROGRAM _CYCLIC
	
	cycleCounter := cycleCounter + 1;
	goodProducts := REAL_TO_UDINT(0.9 * cycleCounter);
	badProducts := cycleCounter - goodProducts;	
	 
END_PROGRAM

