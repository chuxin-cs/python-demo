import { Injectable } from '@nestjs/common';
import { CreateXxxDto } from './dto/create-xxx.dto';
import { UpdateXxxDto } from './dto/update-xxx.dto';

@Injectable()
export class XxxService {
  create(createXxxDto: CreateXxxDto) {
    return 'This action adds a new xxx';
  }

  findAll() {
    return `This action returns all xxx`;
  }

  findOne(id: number) {
    return `This action returns a #${id} xxx`;
  }

  update(id: number, updateXxxDto: UpdateXxxDto) {
    return `This action updates a #${id} xxx`;
  }

  remove(id: number) {
    return `This action removes a #${id} xxx`;
  }
}
