import {
  Body,
  Controller,
  Get,
  Inject,
  Param,
  Post,
  Query,
} from '@nestjs/common';
import { UserService } from '../service/UserService';
import { JWTService } from '../service/JWTService';

class UserDto {
  name: string;
  password: string;
}

@Controller('user')
export class UserController {
  constructor(
    // private readonly userService: UserService,
    private readonly jwtService: JWTService,
  ) {}

  // 通过 Inject 的注入方式  和 在 constructor 中功能是一样的
  @Inject(UserService)
  private readonly userService: UserService;

  // @Inject(JWTService)
  // private readonly jWTService: JWTService;

  // 通过 @Param 取 url 中的参数，比如 /userInfo/111 里的 111
  @Get('/userInfo/:id')
  getUser(@Param('id') id: string): string {
    return this.userService.getUser() + '-' + id + this.jwtService.getName();
  }

  // 通过 @Query 来取 url 中的 query 参数，比如 /user/userData?id=222 里的 222
  @Get('/userData')
  getUserData(@Query('id') id: string): string {
    return this.userService.getUser() + id;
  }

  // 请求体一般会传递 json，比如 { username: 'xxx', password: 'xxx' }
  @Post('/add')
  addUser(@Body() userDto: UserDto): string {
    return 'add user' + JSON.stringify(userDto);
  }
}
