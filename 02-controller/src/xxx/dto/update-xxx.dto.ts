import { PartialType } from '@nestjs/mapped-types';
import { CreateXxxDto } from './create-xxx.dto';

export class UpdateXxxDto extends PartialType(CreateXxxDto) {}
