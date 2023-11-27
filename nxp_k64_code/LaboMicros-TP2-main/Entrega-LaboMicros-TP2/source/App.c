/***************************************************************************//**
  @file     App.c
  @brief    Application functions
  @author   Nicolás Magliola
 ******************************************************************************/

/*******************************************************************************
 * INCLUDE HEADER FILES
 ******************************************************************************/

#include "board.h"
#include "gpio.h"
#include "uart_drv.h"
#include <string.h>
#include "i2cm.h"
#include "timer.h"
#include "FXOS8700CQ.h"
#include "SPI_DRV.h"
#include "DRV_MCP25625.h"




/*******************************************************************************
 * CONSTANT AND MACRO DEFINITIONS USING #DEFINE
 ******************************************************************************/

/*******************************************************************************
 * FUNCTION PROTOTYPES FOR PRIVATE FUNCTIONS WITH FILE LEVEL SCOPE
 ******************************************************************************/


void create_pc_string(int cant, char*out_str);
void create_send_string(char*out_str);
void printUartData();
void package_own_data(void);
int send_own_info(void);
int receive_info(void);
void decodeMessage(int groupnum, char* array);
int power(int pow, int num);

/*******************************************************************************
 *******************************************************************************
                        GLOBAL FUNCTION DEFINITIONS
 *******************************************************************************
 ******************************************************************************/

char numerstring[15];

/* Función que se llama 1 vez, al comienzo del programa */
void App_Init (void)
{

	//init_I2C(I2C_0);
	int a = accel_mag_init();
	while(a == init_ERROR)
	{
		a = accel_mag_init();
	}

	*(numerstring) = 'X';
	*(numerstring+7) = 'Y';
	numerstring [14] = '\n';
	UART_Init(9600, 1);
	timerInit();
	timerStart(timerGetId(), TIMER_MS2TICKS(60), TIM_MODE_PERIODIC, printUartData);

}

/* Función que se llama constantemente en un ciclo infinito */



void App_Run (void)
{

		package_own_data();
}


/*******************************************************************************
 *******************************************************************************
                        LOCAL FUNCTION DEFINITIONS
 *******************************************************************************
 ******************************************************************************/

void uint16ToAsciiChars(int16_t value, char* result) {
    // Handle the sign
    char signChar = (value < 0) ? '-' : '+';
    value = (value < 0) ? -value : value;

    // Extract individual digits
    int digit[5];
    digit[4] = value % 10; value /= 10;
    digit[3] = value % 10; value /= 10;
    digit[2] = value % 10; value /= 10;
    digit[1] = value % 10; value /= 10;
    digit[0] = value % 10;

    // Convert digits to ASCII characters
    for (int i = 0; i < 5; ++i) {
        result[i+1] = '0' + digit[i];
    }

    // Insert sign character
    result[0] = signChar;

}

void package_own_data(){

	static SRAWDATA accel;
	static SRAWDATA magn;
	static angular_data_t angs;
	read_accel_data();
	int a = is_accel_data_ready(&accel, &magn);
	if (a)
	{
		angs = raw_2_angles(&accel, &magn);

	}

	uint16ToAsciiChars(angs.roll, numerstring+1);
	uint16ToAsciiChars(angs.pitch, numerstring+8);

	}

void printUartData(){
	UART_Send_Data(numerstring, 15);
	return;
}


