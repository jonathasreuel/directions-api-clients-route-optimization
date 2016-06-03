#import "SWGService.h"

@implementation SWGService

/**
 * Maps json key to property name.
 * This method is used by `JSONModel`.
 */
+ (JSONKeyMapper *)keyMapper
{
  return [[JSONKeyMapper alloc] initWithDictionary:@{ @"id": @"_id", @"type": @"type", @"name": @"name", @"address": @"address", @"duration": @"duration", @"time_windows": @"timeWindows", @"size": @"size", @"required_skills": @"requiredSkills", @"allowed_vehicles": @"allowedVehicles" }];
}

/**
 * Indicates whether the property with the given name is optional.
 * If `propertyName` is optional, then return `YES`, otherwise return `NO`.
 * This method is used by `JSONModel`.
 */
+ (BOOL)propertyIsOptional:(NSString *)propertyName
{
  NSArray *optionalProperties = @[@"_id", @"type", @"name", @"address", @"duration", @"timeWindows", @"size", @"requiredSkills", @"allowedVehicles"];

  if ([optionalProperties containsObject:propertyName]) {
    return YES;
  }
  else {
    return NO;
  }
}

/**
 * Gets the string presentation of the object.
 * This method will be called when logging model object using `NSLog`.
 */
- (NSString *)description {
    return [[self toDictionary] description];
}

@end
