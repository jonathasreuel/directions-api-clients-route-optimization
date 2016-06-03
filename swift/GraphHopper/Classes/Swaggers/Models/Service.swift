//
// Service.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation


public class Service: JSONEncodable {

    public enum SwaggerType: String { 
        case Service = "service"
        case Pickup = "pickup"
        case Delivery = "delivery"
    }
    
    /** Unique identifier of service */
    public var id: String?
    /** type of service */
    public var type: SwaggerType?
    /** name of service */
    public var name: String?
    public var address: Address?
    /** duration of service, i.e. time in ms the corresponding activity takes */
    public var duration: Int?
    /** array of time windows. currently, only a single time window is allowed */
    public var time_windows: [TimeWindow]?
    /** array of capacity dimensions */
    public var size: [Int]?
    /** array of required skills */
    public var required_skills: [String]?
    /** array of allowed vehicle ids */
    public var allowed_vehicles: [String]?
    

    // MARK: JSONEncodable
    func encodeToJSON() -> AnyObject {
        var nillableDictionary = [String:AnyObject?]()
        nillableDictionary["id"] = self.id
        nillableDictionary["type"] = self.type?.rawValue
        nillableDictionary["name"] = self.name
        nillableDictionary["address"] = self.address?.encodeToJSON()
        nillableDictionary["duration"] = self.duration
        nillableDictionary["time_windows"] = self.time_windows?.encodeToJSON()
        nillableDictionary["size"] = self.size?.encodeToJSON()
        nillableDictionary["required_skills"] = self.required_skills?.encodeToJSON()
        nillableDictionary["allowed_vehicles"] = self.allowed_vehicles?.encodeToJSON()
        let dictionary: [String:AnyObject] = APIHelper.rejectNil(nillableDictionary) ?? [:]
        return dictionary
    }
}
