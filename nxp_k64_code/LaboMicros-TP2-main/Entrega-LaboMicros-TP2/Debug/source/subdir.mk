################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../source/App.c \
../source/DRV_MCP25625.c \
../source/FXOS8700CQ.c \
../source/SPI_DRV.c \
../source/SysTick.c \
../source/gpio.c \
../source/i2cm.c \
../source/timer.c \
../source/uart_drv.c 

OBJS += \
./source/App.o \
./source/DRV_MCP25625.o \
./source/FXOS8700CQ.o \
./source/SPI_DRV.o \
./source/SysTick.o \
./source/gpio.o \
./source/i2cm.o \
./source/timer.o \
./source/uart_drv.o 

C_DEPS += \
./source/App.d \
./source/DRV_MCP25625.d \
./source/FXOS8700CQ.d \
./source/SPI_DRV.d \
./source/SysTick.d \
./source/gpio.d \
./source/i2cm.d \
./source/timer.d \
./source/uart_drv.d 


# Each subdirectory must supply rules for building sources it contributes
source/%.o: ../source/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -DCPU_MK64FN1M0VLL12 -D__USE_CMSIS -DDEBUG -I../source -I../ -I../SDK/CMSIS -I../SDK/startup -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -mcpu=cortex-m4 -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


