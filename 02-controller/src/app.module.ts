import { Module } from '@nestjs/common';
import { UserController } from './controller/UserController';
import { UserService } from './service/UserService';
import { JWTService } from './service/JWTService';
import { AaaController } from './aaa/aaa.controller';
import { AaaService } from './aaa/aaa.service';
import { XxxModule } from './xxx/xxx.module';

@Module({
  imports: [XxxModule],
  controllers: [UserController, AaaController],
  providers: [UserService, JWTService, AaaService],
})
export class AppModule {}
