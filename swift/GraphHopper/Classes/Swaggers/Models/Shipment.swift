//
// Shipment.swift
//
// Generated by swagger-codegen
// https://github.com/swagger-api/swagger-codegen
//

import Foundation


public class Shipment: JSONEncodable {

    /** Unique identifier of service */
    public var id: String?
    /** name of shipment */
    public var name: String?
    public var pickup: Stop?
    public var delivery: Stop?
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
        nillableDictionary["name"] = self.name
        nillableDictionary["pickup"] = self.pickup?.encodeToJSON()
        nillableDictionary["delivery"] = self.delivery?.encodeToJSON()
        nillableDictionary["size"] = self.size?.encodeToJSON()
        nillableDictionary["required_skills"] = self.required_skills?.encodeToJSON()
        nillableDictionary["allowed_vehicles"] = self.allowed_vehicles?.encodeToJSON()
        let dictionary: [String:AnyObject] = APIHelper.rejectNil(nillableDictionary) ?? [:]
        return dictionary
    }
}
