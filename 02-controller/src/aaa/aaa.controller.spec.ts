import { Test, TestingModule } from '@nestjs/testing';
import { AaaController } from './aaa.controller';

describe('AaaController', () => {
  let controller: AaaController;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [AaaController],
    }).compile();

    controller = module.get<AaaController>(AaaController);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });
});
