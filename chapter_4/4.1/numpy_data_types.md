# NumPys data types
__________________________________________________________________________________________________________________________________________________________
type		| type code | Description							  	 							|
---------------|:----------|:----------------------------------------------------------------------------------------------------------------------------:|
int9, uint8	| i1, u1    | signed and unsigned 8-bit (1 byte) integer types			 							|
int16, uint16	| i2, u2    | signed and unsigned 16-bit integer types				 							|
int32, uint32	| i4, u4    | signed and unsigned 32-bit integer types 			  	 							|
int64, uint64 	| i8, u8    | signed and unsigned 32-bit integer types 			  	 							|
float16	| f2	    | half-precision floating point  					  	 							|
float32	|f4 or f    | standard single-precision floating point; compatible with C float	 							|
float64	| f8 or d   | standard double-precision floating point; compatible with C float and python float object					|
float128	| f16 or g  | Extended precision floating point				  	 							|
complex64	| c8, c16   | complex numbers represented by two 32, 64 or 128 floats, respectively   							|
complex128	| c32	    | 										 							|
complex256	|	    |										 							|
bool		| ?	    | boolean type storing True and False values				 							|
object		| 0	    | python object type; a value can be any python object			 							|
string_	| S	    | Fixed-length ASCII string type (1 byte per character); for example to to create a string dtype with length 10, use 's10'	|
unicode_	| U	    | Fixed length unicode type (number of bytes, plstform specific), same specification semantics as a string_ (e.g., 'U10')	|
-----------------------------------------------------------------------------------------------------------------------------------------------------------	        
