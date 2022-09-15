import numpy as np

def convert_ucf_to_h(_name, _path_ucf, _path_h):

	data = ['// Leka - LekaOS\n',
			'// Copyright 2022 APF France handicap\n',
			'// SPDX-License-Identifier: Apache-2.0\n\n',
			'// clang-format off\n',
			'/* Define to prevent recursive inclusion -------- */\n\n',
			'#ifndef MLC_CONFIGURATION_H\n',
			'#define MLC_CONFIGURATION_H\n\n'
	]

	data_file = open(_path_h, "a")
	
	for d in data:
		data_file.write(d)
		

	include = ["/* Includes ------------------ */\n",
				"#include <array>\n",
				"#include <cstdint>\n"]
	
	for i in include:
		data_file.write(i)

	struct_data = ["/** Common data block definition **/\n",
					"struct imu_register{\n",
					"\tuint8_t address; \n",
  					"\tuint8_t data;\n",
					"};\n\n"
	]
	
	for s in struct_data:
		data_file.write(s)


	ucf_file = open(_path_ucf, "r")
	data_ucf = ucf_file.readlines()
	data_struct_ucf = []
	
	#essayer de récupérer l'indice de début du Ac
	
	for i in range(4,len(data_ucf)):
		data_struct_ucf.append(data_ucf[i].split(" ")) #243,3
		data_struct_ucf_f = np.delete(data_struct_ucf, 0,1) #243,2
		

	proto_struct = "/** Configuration array generated from Unico Tool **/\n"
	reg_struct = "inline constexpr auto " + _name + " = std::to_array<imu_register>({" + '\n'
	start_struct = [proto_struct, reg_struct]

	for l in start_struct:
		data_file.write(l)
	
	for i in range(len(data_struct_ucf_f)):
		data_struct_ucf_f[i][1] = data_struct_ucf_f[i][1].strip("\n")
		string = "\t{.address = 0x" + data_struct_ucf_f[i][0] + ", .data = 0x" + data_struct_ucf_f[i][1] + " ,},\n"
		data_file.write(string)
	

	end_of_h_file = ["});\n\n",
					"#endif\n\n",
					"// clang-format on"]
	
	for e in end_of_h_file:
		data_file.write(e)


	data_file.close()
	ucf_file.close()

if __name__ == "__main__":
	convert_ucf_to_h("test_ucf_file_to_h")
	