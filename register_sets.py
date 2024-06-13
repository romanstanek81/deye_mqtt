from deye_controller.modbus.protocol import *


read_regs_supported = [attr[1] for attr in HoldingRegisters.__dict__.items() if not attr[0].startswith('__') and attr[0] != 'as_list' and isinstance(attr[1], tuple({IntType, FloatType, BoolType, LongType}))]

read_write_reg_map = {}
wr_map = {}
for name, obj in WritableRegisters.__dict__.items():
    if not name.startswith('__') and hasattr(obj, 'address'):
        wr_map[obj.address] = obj

for name, obj in HoldingRegisters.__dict__.items():
    if not name.startswith('__') and hasattr(obj, 'address'):
        if obj.address in wr_map:
            read_write_reg_map[obj.description.lower()] = wr_map[obj.address]

