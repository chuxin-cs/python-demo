import { Module } from '@nestjs/common';
import { XxxService } from './xxx.service';
import { XxxController } from './xxx.controller';

@Module({
  controllers: [XxxController],
  providers: [XxxService],
})
export class XxxModule {}
