import { Test, TestingModule } from '@nestjs/testing';
import { XxxController } from './xxx.controller';
import { XxxService } from './xxx.service';

describe('XxxController', () => {
  let controller: XxxController;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [XxxController],
      providers: [XxxService],
    }).compile();

    controller = module.get<XxxController>(XxxController);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });
});
