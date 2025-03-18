import {
  Controller,
  Get,
  Post,
  Body,
  Patch,
  Param,
  Delete,
} from '@nestjs/common';
import { XxxService } from './xxx.service';
import { CreateXxxDto } from './dto/create-xxx.dto';
import { UpdateXxxDto } from './dto/update-xxx.dto';

@Controller('xxx')
export class XxxController {
  constructor(private readonly xxxService: XxxService) {}

  @Post()
  create(@Body() createXxxDto: CreateXxxDto) {
    return this.xxxService.create(createXxxDto);
  }

  @Get()
  findAll() {
    return this.xxxService.findAll();
  }

  @Get(':id')
  findOne(@Param('id') id: string) {
    return this.xxxService.findOne(+id);
  }

  @Patch(':id')
  update(@Param('id') id: string, @Body() updateXxxDto: UpdateXxxDto) {
    return this.xxxService.update(+id, updateXxxDto);
  }

  @Delete(':id')
  remove(@Param('id') id: string) {
    return this.xxxService.remove(+id);
  }
}
